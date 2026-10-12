# Estatística Descritiva e Inferencial em Python para Humanidades

Notebooks e fontes do [site do curso](https://jhlopesalves.github.io/eda_humanidades/), ministrado por Jhonatan H. Lopes. O repositório contém os Encontros 1–10, o Datasaurus Dozen e a segunda parte do Encontro 8: doze notebooks de aula, além de dados, tarefas e gabaritos disponíveis.

A sequência e os exemplos preservam o curso ministrado. O site é gerado pelo Quarto com as saídas salvas dos notebooks; a renderização não executa Python. Para estudar e executar os exemplos no navegador, use o link do Google Colab no início de cada aula.

## Renderização local

Instale o [Quarto](https://quarto.org/docs/get-started/) 1.10.18, versão usada na verificação local e fixada no workflow do GitHub Pages. Na raiz do repositório:

```bash
quarto preview
```

Para gerar os arquivos estáticos em `_site/`:

```bash
quarto render
```

Não é necessário instalar as bibliotecas Python para gerar o site. `execute.enabled: false` em `_quarto.yml` mantém separadas a execução dos notebooks e a publicação de suas saídas.

## Execução e verificação dos notebooks

O ambiente local foi verificado com Python 3.14.7. As dependências diretas usadas estão fixadas em `requirements-notebooks.txt`; isso registra o ambiente testado, sem garantir resultados idênticos em outros sistemas ou no Colab.

Com [uv](https://docs.astral.sh/uv/):

```bash
uv venv --python 3.14
uv pip install -r requirements-notebooks.txt
uv run python scripts/check_course.py
```

O último comando verifica o formato dos notebooks, a sequência das contagens de execução e os erros salvos. Depois de `quarto render`, verifique também as páginas, figuras e links locais:

```bash
uv run python scripts/check_course.py --site
```

Para executar todas as aulas em kernels novos e verificar exemplos numéricos:

```bash
uv run python scripts/check_course.py --execute
```

Essa verificação usa os arquivos locais, executa cada notebook em seu próprio diretório e não altera as fontes nem as saídas salvas. O `KeyError` do Encontro 2 é intencional e está marcado com a tag `raises-exception`. Outros erros interrompem a verificação. Para editar e renovar saídas, abra os notebooks em um kernel deste ambiente no Jupyter ou no VS Code e execute as células em ordem, interpretando o erro deliberado.

## Estrutura

| Caminho | Conteúdo |
| :--- | :--- |
| `encontro_1/` a `encontro_10/` | Notebooks de aula; `data/` e `homework/` onde existem |
| `encontro_5/datasaurus.ipynb` | Demonstração metodológica com o Datasaurus Dozen |
| `encontro_8/enc_8-parte2.ipynb` | Associação e visualização com o Gapminder |
| `index.qmd`, `about.qmd` | Página inicial e informações sobre o curso |
| `_quarto.yml`, `styles.css` | Renderização, navegação e apresentação |
| `DATASETS.md` | Fontes, transformações conhecidas e lacunas de proveniência |
| `scripts/check_course.py` | Verificações de fontes, execução e site renderizado |
| `.github/workflows/publish.yml` | Publicação no GitHub Pages após alterações em `main` |

Os arquivos de `_site/`, `.quarto/` e `.venv/` são locais e ignorados pelo Git. A lista explícita em `_quarto.yml` publica as aulas e as páginas do curso; tarefas e gabaritos continuam acessíveis pelos links das aulas.

## Manutenção

Ao alterar uma aula, mantenha legíveis tanto o notebook quanto sua página estática. Preserve as implementações introdutórias e os erros que demonstram conceitos; use comentários `#|` apenas para opções de apresentação do Quarto. Mudanças de código exigem nova execução e revisão das saídas. Mudanças de títulos, links ou CSS exigem renderização e inspeção no navegador, inclusive em tela estreita e nos dois temas.

O [registro da revisão para publicação](docs/publication-review.md) descreve as correções, a verificação e as limitações desta passagem. As tarefas e os gabaritos não passaram por uma revisão pedagógica completa.

## Licença

A [licença MIT](LICENSE) existente aplica-se ao material autoral. Textos, imagens, metadados e conjuntos de dados de terceiros mantêm os termos de suas fontes; a presença no repositório não os relicencia. Consulte [DATASETS.md](DATASETS.md) antes de redistribuí-los.
