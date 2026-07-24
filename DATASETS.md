# Catálogo de dados

Este documento separa fatos verificáveis no repositório de informações de proveniência que não foram preservadas. Quando o histórico não contém a URL de aquisição, a data de download, o script de transformação ou uma licença, a lacuna é indicada explicitamente.

## Textos literários — `encontro_3/data/`

| Arquivo | Obra indicada no arquivo | Uso atual |
| :--- | :--- | :--- |
| `crime_and_punishment.txt` | *Crime and Punishment*, Fyodor Dostoyevsky, eBook 2554 | Tarefa e gabarito do Encontro 3 |
| `dom_casmurro.txt` | *Dom Casmurro*, Machado de Assis | Tarefa e gabarito do Encontro 3 |
| `leonardo_da_vinci.txt` | *The Notebooks of Leonardo Da Vinci — Complete* | Tarefa e gabarito do Encontro 3 |
| `memorias_postumas.txt` | *Memorias Posthumas de Braz Cubas*, Machado de Assis | Tarefa e gabarito do Encontro 3 |
| `shakespeare.txt` | *The Complete Works of William Shakespeare* | Tarefa e gabarito do Encontro 3 |

- Fonte identificável no conteúdo: [Project Gutenberg](https://www.gutenberg.org/).
- `crime_and_punishment.txt` conserva o cabeçalho, o identificador 2554 e os créditos. Os outros quatro arquivos começam depois do cabeçalho original, mas conservam o marcador final e os termos do Project Gutenberg.
- O repositório não conserva os identificadores do Gutenberg, datas de download nem o procedimento de remoção dos cabeçalhos dos outros quatro arquivos. Não é possível reconstruir esses detalhes com segurança apenas pelo histórico disponível.
- O Project Gutenberg publica avisos territoriais e condições de uso próprios. A condição jurídica de uma obra pode variar conforme o país; consulte o texto de licença incorporado a cada arquivo e a página da obra antes de redistribuí-la.

## Gapminder — `encontro_4/data/gapminderDataFiveYear.csv`

- 1.704 observações, uma por país e ano, com as colunas `country`, `year`, `pop`, `continent`, `lifeExp` e `gdpPercap`.
- Abrange anos quinquenais de 1952 a 2007 e é descrito no material como o recorte clássico popularizado pelo pacote `gapminder` do R.
- Uso atual: tarefa e gabarito do Encontro 4. Os notebooks leem a cópia deste repositório por uma URL `raw`.
- Fonte conceitual indicada no material: [Gapminder Foundation](https://www.gapminder.org/data/).
- A URL original de aquisição, a data do download, eventuais transformações e a licença específica desta cópia não estão registradas no histórico. Consulte a fonte antes de redistribuir.

## Metadados de livros — `encontro_4/data/goodreads.csv`

- 10.537 linhas e 12 colunas, incluindo título, autoria, avaliação média, ISBN, número de páginas, contagens de avaliações e resenhas, data de publicação e editora.
- O arquivo foi renomeado e ajustado em commits anteriores; a coluna `publisher_family` está presente na versão atual.
- Não há notebook atual que leia esse arquivo. Ele permanece como material de apoio ou para uso futuro.
- O histórico local não registra uma página-fonte confiável, data de aquisição, transformação reproduzível ou licença. O nome e o esquema sugerem metadados associados ao Goodreads, mas isso não basta para atribuir uma origem ou licença precisa. Redistribua somente após verificar esses pontos.

## arXiv — `encontro_5/data/`

| Arquivo | Conteúdo observável | Uso atual |
| :--- | :--- | :--- |
| `arxiv_subset.csv` | 78.148 registros de 2020–2025 e 148 categorias primárias | Fonte intermediária preservada |
| `arxiv_eda_papers.csv` | 3.387 artigos em nove categorias primárias, com rótulos e contagens derivadas | Encontros 5 e 6 |
| `arxiv_eda_categories_long.csv` | Categorias explodidas, uma linha por associação artigo–categoria | Não referenciado nos notebooks atuais |
| `arxiv_eda_category_year_counts.csv` | Contagens por ano e categoria primária | Não referenciado nos notebooks atuais |
| `arxiv_eda_year_counts.csv` | Contagens por ano e área de primeiro nível | Não referenciado nos notebooks atuais |

- Os 3.387 identificadores de `arxiv_eda_papers.csv` existem em `arxiv_subset.csv`; `paper_id` deve ser tratado como texto, não como número.
- A tabela didática acrescenta campos como prévia do resumo, rótulos legíveis, década e números de palavras/categorias. As tabelas menores são compatíveis com formas longa e agregada desse recorte.
- O histórico não inclui o script que selecionou as nove categorias nem a regra completa de amostragem. Em particular, `stat.ML` tem 1.000 linhas na tabela didática, mas não há evidência suficiente para afirmar como esse limite foi escolhido. Também não há URL de aquisição, data de extração ou licença registrada para a cópia intermediária.
- Os metadados remetem ao [arXiv](https://arxiv.org/), mas os direitos de cada resumo e artigo continuam associados aos respectivos autores e licenças. Consulte os termos do arXiv antes de redistribuir os arquivos.

## Datasaurus — dependência remota

`encontro_5/datasaurus.ipynb` lê `datasaurus.csv` diretamente do repositório público [TidyTuesday de 13 de outubro de 2020](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-10-13). Não há cópia local no repositório. O notebook usa os conjuntos construídos para mostrar que resumos marginais semelhantes podem ocultar formas bidimensionais muito diferentes.

## Verificações locais

Para conferir quantidade de linhas sem carregar os arquivos inteiros em memória:

```bash
wc -l encontro_3/data/*.txt encontro_4/data/*.csv encontro_5/data/*.csv
```

Para registrar a identidade exata das cópias usadas em uma análise:

```bash
sha256sum encontro_3/data/*.txt encontro_4/data/*.csv encontro_5/data/*.csv
```

Esses comandos verificam os arquivos presentes, mas não preenchem as lacunas de proveniência descritas acima.
