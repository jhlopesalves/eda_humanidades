"""Check published notebooks, optional fresh execution and rendered local links.

Run from any directory. Fresh execution keeps results in memory and uses each
lesson's directory so its existing relative data paths retain their meaning.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import nbformat
import yaml
from bs4 import BeautifulSoup
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ERROR = ("KeyError", "'preposição'")

# These checks compare independent implementations and known data invariants.
# They stay outside the teaching cells and are never saved into the notebooks.
CHECKS = {
    "encontro_1/enc_1.ipynb": """
assert diferenca_entre_anos == ano_morte - ano_nascimento
""",
    "encontro_2/enc_2.ipynb": """
assert 'preposição' not in frequencias
assert media == sum(valores) / len(valores)
""",
    "encontro_3/enc_3.ipynb": """
import statistics
assert frequencias_explicitas == frequencias
assert sum(frequencias.values()) == len(tokens_mertonian)
assert 1 / len(tokens_mertonian) <= ttr_mertonian <= 1
assert calcular_média([1, 2, 9]) == statistics.mean([1, 2, 9])
assert calcular_mediana([9, 1, 2]) == statistics.median([9, 1, 2])
assert calcular_mediana([9, 1, 2, 8]) == statistics.median([9, 1, 2, 8])
assert calcular_ttr(['a', 'a', 'a']) == 1/3
assert calcular_ttr(['a', 'b', 'c']) == 1
""",
    "encontro_4/enc_4.ipynb": """
assert (obras_df['n_types'] <= obras_df['n_tokens']).all()
assert (obras_df['n_tokens'] > 0).all()
assert np.allclose(obras_df['ttr'], obras_df['n_types'] / obras_df['n_tokens'])
""",
    "encontro_5/enc_5.ipynb": """
assert len(arxiv_df) == 3387
assert np.isclose(sample_variance, np.var(values, ddof=1))
assert np.isclose(sample_standard_deviation, np.std(values, ddof=1))
assert np.isclose(var_categories, arxiv_df['n_categories'].var(ddof=1))
""",
    "encontro_6/enc_6.ipynb": """
assert normalised_shannon_entropy(pd.Series(['a', 'a'])) == 0
assert np.isclose(normalised_shannon_entropy(pd.Series(['a', 'b'])), 1)
assert np.isclose(normalised_shannon_entropy(pd.Series(['a', None])), 1)
try:
    normalised_shannon_entropy(pd.Series([], dtype='object'))
except ValueError:
    pass
else:
    raise AssertionError('Empty entropy must be undefined')
assert 0 <= norm_entropy_categories <= 1
""",
    "encontro_7/enc_7.ipynb": """
assert len(longcat_authors) == 182
assert arxiv_df['n_authors'].max() == len(longcat_authors)
assert (author_counts > 0).all()
""",
    "encontro_8/enc_8.ipynb": """
assert np.isclose(pearson_between_ranks.statistic, authors_abstract_spearman.statistic)
assert len(without_max_authors) == len(arxiv_df) - 1
assert len(gapminder_2007) == 142
assert np.allclose(np.diag(arxiv_spearman_matrix), 1)
""",
    "encontro_8/enc_8-parte2.ipynb": """
import numpy as np
assert len(gapminder_2007) == 142
assert np.isclose(
    gdp_life_spearman.statistic,
    gapminder_2007['gdpPercap'].corr(
        gapminder_2007['lifeExp'], method='spearman'
    ),
)
assert len(ax.artists) == 0
assert ax.get_legend().get_title().get_text() == 'Continentes'
assert len(population_labels) > 1
""",
    "encontro_9/enc_9.ipynb": """
assert len(gaussian_values) == n_observacoes
assert abs(sample_mean) < 0.05
assert abs(sample_std - 1) < 0.05
assert np.isclose(stats.norm.cdf(0), 0.5)
""",
    "encontro_10/enc_10.ipynb": """
assert n_observations == 397 and k_vpo == 247
assert np.isclose(p_hat, 247/397)
assert np.isclose(model_standard_error, np.sqrt(p_hat * (1-p_hat) / n_observations))
assert np.allclose(standard_errors[1:], standard_errors[:-1] / 2)
assert (
    0 <= bootstrap_result.confidence_interval.low
    < p_hat < bootstrap_result.confidence_interval.high <= 1
)
assert abs(bootstrap_result.standard_error - model_standard_error) < 0.002
""",
    "encontro_5/datasaurus.ipynb": """
assert len(datasaurus_df) == 1846
assert datasaurus_df['dataset'].nunique() == 13
assert (datasaurus_df.groupby('dataset').size() == 142).all()
assert np.isclose(cohens_d(np.array([1, 2, 3]), np.array([2, 3, 4])), -1)
""",
}


def check_execution_state(notebook: nbformat.NotebookNode, path: Path) -> int:
    """Validate saved or newly executed counts and the one deliberate error."""
    cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    counts = [cell.execution_count for cell in cells]
    if counts != list(range(1, len(cells) + 1)):
        raise ValueError(f"{path}: inconsistent execution counts: {counts}")
    errors = []
    for cell in cells:
        for output in cell.outputs:
            if output.output_type == "error":
                error = (output.ename, output.evalue)
                if "raises-exception" not in cell.metadata.get("tags", []):
                    raise ValueError(f"{path}: unmarked error: {error}")
                errors.append(error)
    expected = [EXPECTED_ERROR] if path.name == "enc_2.ipynb" else []
    if errors != expected:
        raise ValueError(f"{path}: expected {expected}, found {errors}")
    return len(cells)


def check_notebook(path: Path, execute: bool) -> int:
    """Check format/state and optionally execute in a fresh local kernel."""
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    code_count = check_execution_state(notebook, path)
    if execute:
        relative = path.relative_to(ROOT).as_posix()
        extra = nbformat.v4.new_code_cell(CHECKS[relative])
        if notebook.nbformat_minor < 5:
            extra.pop("id", None)
        notebook.cells.append(extra)
        client = NotebookClient(
            notebook,
            timeout=600,
            kernel_name="python3",
            allow_errors=False,
            record_timing=False,
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.execute()
        notebook.cells.pop()
        check_execution_state(notebook, path)
        warnings = [
            output.text
            for cell in notebook.cells
            for output in cell.get("outputs", [])
            if output.get("name") == "stderr"
        ]
        if warnings:
            print(f"STDERR {relative}: {warnings}", file=sys.stderr)
    print(f"PASS {path.relative_to(ROOT)} ({code_count} code cells)", flush=True)
    return code_count


def check_site(sources: list[str]) -> None:
    """Check configured pages, image descriptions and local resource targets."""
    site = ROOT / "_site"
    documents: dict[Path, BeautifulSoup] = {}
    figures = 0
    links = 0

    def document(path: Path) -> BeautifulSoup:
        path = path.resolve()
        if path not in documents:
            documents[path] = BeautifulSoup(path.read_text(), "html.parser")
        return documents[path]

    for source in sources:
        page = site / Path(source).with_suffix(".html")
        soup = document(page)
        main = soup.select_one("main")
        if main is None or len(main.select("h1")) != 1:
            raise ValueError(f"{page}: expected one main heading")
        if source.endswith(".ipynb"):
            if not main.select_one('img[alt="Abrir no Google Colab"]'):
                raise ValueError(f"{page}: missing Portuguese Colab description")
            if not main.select_one(".lesson-runtime-note"):
                raise ValueError(f"{page}: missing saved-output explanation")
            if soup.title is None or soup.title.get_text().startswith(
                ("enc_", "datasaurus –")
            ):
                raise ValueError(f"{page}: filename used as page title")
        for image in main.select("img"):
            if not image.get("alt", "").strip():
                raise ValueError(f"{page}: missing image description")
            if "figure-html" in image.get("src", ""):
                figure = image.find_parent("figure")
                if figure is None or figure.select_one("figcaption") is None:
                    raise ValueError(f"{page}: missing plot caption")
                figures += 1
        for element in soup.select("[href], [src]"):
            for attribute in ("href", "src"):
                value = element.get(attribute)
                if not value:
                    continue
                parts = urlsplit(value)
                if parts.scheme or parts.netloc:
                    continue
                local = unquote(parts.path)
                if local.startswith("/"):
                    target = site / local.lstrip("/")
                elif local:
                    target = page.parent / local
                else:
                    target = page
                target = target.resolve()
                if target.is_dir():
                    target /= "index.html"
                if not target.exists():
                    raise ValueError(f"{page}: missing local resource {value}")
                if parts.fragment and target.suffix == ".html":
                    target_soup = document(target)
                    fragment = unquote(parts.fragment)
                    if not target_soup.find(id=fragment) and not target_soup.find(
                        attrs={"name": fragment}
                    ):
                        raise ValueError(f"{page}: missing anchor {value}")
                links += 1
    homepage = document(site / "index.html")
    if homepage.select(".resource-grid, .resource-card") or homepage.find(
        ["h1", "h2", "h3"], string="Materiais"
    ):
        raise ValueError("Homepage: obsolete Materiais section")
    print(
        f"PASS site: {len(sources)} pages, {figures} plots, "
        f"{links} local links/resources"
    )


def main() -> None:
    """Run the selected checks without changing source files or saved outputs."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="execute fresh kernels")
    parser.add_argument("--site", action="store_true", help="check the rendered _site")
    arguments = parser.parse_args()
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text())
    sources = config["project"]["render"]
    # The kernelspec launches `python`; select the interpreter of this environment.
    environment_bin = str(Path(sys.executable).parent)
    os.environ["PATH"] = environment_bin + os.pathsep + os.environ["PATH"]
    count = 0
    notebooks = [ROOT / source for source in sources if source.endswith(".ipynb")]
    for path in notebooks:
        count += check_notebook(path, arguments.execute)
    print(f"PASS notebooks: {len(notebooks)} notebooks, {count} code cells")
    if arguments.site:
        check_site(sources)


if __name__ == "__main__":
    main()
