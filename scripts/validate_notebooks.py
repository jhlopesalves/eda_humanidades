#!/usr/bin/env python3
"""Valida estrutura, sintaxe, execução e links dos notebooks do curso."""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_TARGET_RE = re.compile(
    r"!?\[[^\]]*\]\(([^)]+)\)|(?:href|src)=[\"']([^\"']+)[\"']",
    flags=re.IGNORECASE,
)


def notebook_paths() -> list[Path]:
    return sorted(REPO_ROOT.glob("encontro_*/*.ipynb")) + sorted(
        REPO_ROOT.glob("encontro_*/homework/*.ipynb")
    )


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def is_student_exercise(path: Path) -> bool:
    return path.name.endswith("_homework.ipynb")


def validate_structure(path: Path) -> list[str]:
    problems: list[str] = []

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"JSON inválido: {exc}"]

    if notebook.get("nbformat") != 4:
        problems.append("o campo nbformat deve ser 4")
    if notebook.get("nbformat_minor", 0) < 5:
        problems.append("o campo nbformat_minor deve ser pelo menos 5 para usar ids")

    cells = notebook.get("cells")
    if not isinstance(cells, list):
        return problems + ["o campo cells deve ser uma lista"]

    ids: list[str] = []
    for index, cell in enumerate(cells):
        cell_id = cell.get("id")
        if not isinstance(cell_id, str) or not cell_id.strip():
            problems.append(f"célula {index}: id ausente ou vazio")
        else:
            ids.append(cell_id)

        if cell.get("cell_type") == "code":
            try:
                ast.parse(cell_source(cell), filename=f"{path}:célula {index}")
            except SyntaxError as exc:
                problems.append(
                    f"célula {index}: sintaxe inválida na linha {exc.lineno}: {exc.msg}"
                )
        elif cell.get("cell_type") == "markdown":
            fence_count = sum(
                line.lstrip().startswith("```")
                for line in cell_source(cell).splitlines()
            )
            if fence_count % 2:
                problems.append(f"célula {index}: bloco de código Markdown não fechado")

    duplicate_ids = sorted({cell_id for cell_id in ids if ids.count(cell_id) > 1})
    if duplicate_ids:
        problems.append(f"ids de célula duplicados: {', '.join(duplicate_ids)}")

    kernelspec = notebook.get("metadata", {}).get("kernelspec", {})
    if kernelspec.get("name") != "python3":
        problems.append("metadata.kernelspec.name deve ser 'python3'")

    expected_colab_url = (
        "https://colab.research.google.com/github/jhlopesalves/"
        f"eda_humanidades/blob/main/{path.relative_to(REPO_ROOT).as_posix()}"
    )
    first_cell_source = cell_source(cells[0]) if cells else ""
    if expected_colab_url not in first_cell_source:
        problems.append("o selo inicial do Colab não aponta para este notebook")

    return problems


def markdown_targets(path: Path) -> set[str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    targets: set[str] = set()

    for cell in notebook["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        for match in MARKDOWN_TARGET_RE.finditer(cell_source(cell)):
            target = match.group(1) or match.group(2)
            targets.add(target.strip())

    return targets


def data_urls(path: Path) -> set[str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    urls: set[str] = set()
    assigned_values: dict[str, object] = {}

    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        try:
            tree = ast.parse(cell_source(cell))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names = [target.id for target in targets if isinstance(target, ast.Name)]
            if not any(name.lower().endswith("_url") for name in names):
                continue
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                continue
            for name in names:
                assigned_values[name] = value
            if (
                isinstance(value, str)
                and value.startswith(("http://", "https://"))
                and not any(name.lower().startswith("base_") for name in names)
            ):
                urls.add(value)

    base_urls = [
        value
        for name, value in assigned_values.items()
        if name.lower().endswith("base_url")
        and isinstance(value, str)
        and value.startswith(("http://", "https://"))
    ]
    relative_file_lists = [
        value
        for value in assigned_values.values()
        if isinstance(value, (list, tuple))
        and value
        and all(
            isinstance(item, str) and item.lower().endswith((".csv", ".txt"))
            for item in value
        )
    ]
    for base_url in base_urls:
        for file_list in relative_file_lists:
            urls.update(base_url + item for item in file_list)

    return urls


def check_http_url(url: str, timeout: float) -> str | None:
    headers = {"User-Agent": "eda-humanidades-notebook-validator/1.0"}
    request = Request(url, headers=headers, method="HEAD")

    try:
        with urlopen(request, timeout=timeout) as response:
            if response.status < 400:
                return None
    except HTTPError as exc:
        if exc.code not in {403, 405}:
            return f"HTTP {exc.code}"
    except (URLError, TimeoutError) as exc:
        return str(exc)

    request = Request(url, headers={**headers, "Range": "bytes=0-0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return None if response.status < 400 else f"HTTP {response.status}"
    except HTTPError as exc:
        # Alguns serviços bloqueiam robôs com 403 mesmo quando a página pública existe.
        return None if exc.code == 403 else f"HTTP {exc.code}"
    except (URLError, TimeoutError) as exc:
        return str(exc)


def validate_links(paths: list[Path], timeout: float) -> list[str]:
    problems: list[str] = []
    public_urls: set[str] = set()

    for path in paths:
        for target in markdown_targets(path):
            if target.startswith(("http://", "https://")):
                public_urls.add(target)
            elif target.startswith(("#", "mailto:")):
                continue
            else:
                local_target = (path.parent / unquote(target.split("#", 1)[0])).resolve()
                if not local_target.exists():
                    problems.append(f"{path.relative_to(REPO_ROOT)}: link local ausente: {target}")
        public_urls.update(data_urls(path))

    for markdown_file in (REPO_ROOT / "README.md", REPO_ROOT / "DATASETS.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for target_match in MARKDOWN_TARGET_RE.finditer(text):
            target = (target_match.group(1) or target_match.group(2)).strip()
            if target.startswith(("http://", "https://")):
                public_urls.add(target)
            elif not target.startswith(("#", "mailto:")):
                local_target = (
                    markdown_file.parent / unquote(target.split("#", 1)[0])
                ).resolve()
                if not local_target.exists():
                    problems.append(
                        f"{markdown_file.name}: link local ausente: {target}"
                    )

    for url in sorted(public_urls):
        problem = check_http_url(url, timeout)
        if problem:
            problems.append(f"{url}: {problem}")

    return problems


def execute_notebooks(paths: list[Path], *, timeout: int, write: bool) -> list[str]:
    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError:
        return [
            "a execução requer nbformat e nbclient; instale requirements.txt"
        ]

    os.environ["MPLBACKEND"] = "module://matplotlib_inline.backend_inline"
    problems: list[str] = []

    for path in paths:
        if is_student_exercise(path):
            print(f"ESTRUTURA {path.relative_to(REPO_ROOT)} (tarefa de estudante)")
            continue

        try:
            notebook = nbformat.read(path, as_version=4)
            with tempfile.TemporaryDirectory(prefix="eda-humanidades-") as workdir:
                client = NotebookClient(
                    notebook,
                    timeout=timeout,
                    kernel_name="python3",
                    allow_errors=False,
                    record_timing=False,
                    resources={"metadata": {"path": workdir}},
                )
                client.execute()
            if write:
                # Mantém o estilo serializado já usado no repositório: conteúdo
                # textual em listas de linhas, sem alterar o significado do nbformat.
                for cell in notebook.cells:
                    if isinstance(cell.get("source"), str):
                        cell["source"] = cell["source"].splitlines(keepends=True)
                    for output in cell.get("outputs", []):
                        if isinstance(output.get("text"), str):
                            output["text"] = output["text"].splitlines(keepends=True)
                        for mime_type, value in output.get("data", {}).items():
                            if mime_type.startswith("text/") and isinstance(value, str):
                                output["data"][mime_type] = value.splitlines(keepends=True)
                path.write_text(
                    json.dumps(notebook, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            print(f"EXECUÇÃO OK {path.relative_to(REPO_ROOT)}")
        except Exception as exc:  # nbclient expõe diferentes subclasses por erro
            problems.append(f"{path.relative_to(REPO_ROOT)}: {type(exc).__name__}: {exc}")

    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="executa notebooks de aula e gabaritos; tarefas ficam só na estrutura",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="grava saídas regeneradas; requer --execute",
    )
    parser.add_argument(
        "--links",
        action="store_true",
        help="verifica links locais, páginas públicas e URLs de dados",
    )
    parser.add_argument("--timeout", type=int, default=180)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.write and not args.execute:
        raise SystemExit("--write requer --execute")

    paths = notebook_paths()
    problems: list[str] = []

    for path in paths:
        notebook_problems = validate_structure(path)
        if notebook_problems:
            problems.extend(
                f"{path.relative_to(REPO_ROOT)}: {problem}"
                for problem in notebook_problems
            )
        else:
            print(f"ESTRUTURA OK {path.relative_to(REPO_ROOT)}")

    if args.links:
        problems.extend(validate_links(paths, args.timeout))
    if args.execute:
        problems.extend(execute_notebooks(paths, timeout=args.timeout, write=args.write))

    if problems:
        print("\nFALHAS:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"\nValidação concluída: {len(paths)} notebooks sem falhas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
