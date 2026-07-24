# Catálogo de dados

Este documento registra as fontes conhecidas, o papel dos arquivos no curso, as transformações identificáveis e as lacunas de proveniência. Quando o histórico não preserva uma informação, ela é indicada como não resolvida.

## Textos literários — `encontro_3/data/`

| Arquivo | Obra indicada no arquivo | Papel no curso |
| :--- | :--- | :--- |
| `crime_and_punishment.txt` | *Crime and Punishment*, Fyodor Dostoyevsky, eBook 2554 | Tarefa e gabarito do Encontro 3 |
| `dom_casmurro.txt` | *Dom Casmurro*, Machado de Assis | Tarefa e gabarito do Encontro 3 |
| `leonardo_da_vinci.txt` | *The Notebooks of Leonardo Da Vinci — Complete* | Tarefa e gabarito do Encontro 3 |
| `memorias_postumas.txt` | *Memorias Posthumas de Braz Cubas*, Machado de Assis | Tarefa e gabarito do Encontro 3 |
| `shakespeare.txt` | *The Complete Works of William Shakespeare* | Tarefa e gabarito do Encontro 3 |

A fonte identificável no conteúdo é o [Project Gutenberg](https://www.gutenberg.org/). `crime_and_punishment.txt` conserva o cabeçalho e o identificador 2554; os outros arquivos começam depois do cabeçalho original, mas conservam o marcador final e os termos do projeto. O histórico não registra os demais identificadores, as datas de download nem o procedimento usado para remover os cabeçalhos.

## Gapminder — `encontro_4/data/gapminderDataFiveYear.csv`

O arquivo contém 1.704 observações por país e ano, de 1952 a 2007, com as colunas `country`, `year`, `pop`, `continent`, `lifeExp` e `gdpPercap`. Ele é usado na tarefa e no gabarito do Encontro 4 e corresponde ao recorte clássico associado à [Gapminder Foundation](https://www.gapminder.org/data/).

A URL original de aquisição, a data do download, eventuais transformações e a licença específica desta cópia não estão registradas.

## Metadados de livros — `encontro_4/data/goodreads.csv`

O arquivo contém metadados de livros e inclui a coluna derivada `publisher_family`. Ele permanece como material de apoio, mas não é lido pelos notebooks atuais. O histórico indica que o arquivo foi renomeado e ajustado, porém não preserva uma página-fonte confiável, a data de aquisição, um procedimento completo de transformação ou a licença.

## arXiv — `encontro_5/data/`

| Arquivo | Conteúdo e papel no curso |
| :--- | :--- |
| `arxiv_subset.csv` | Recorte intermediário de metadados de 2020–2025 |
| `arxiv_eda_papers.csv` | Amostra didática usada nos Encontros 5 e 6 |
| `arxiv_eda_categories_long.csv` | Forma longa das associações artigo–categoria |
| `arxiv_eda_category_year_counts.csv` | Contagens por ano e categoria primária |
| `arxiv_eda_year_counts.csv` | Contagens por ano e área de primeiro nível |

Os identificadores de `arxiv_eda_papers.csv` existem em `arxiv_subset.csv`, e `paper_id` deve ser tratado como string. A amostra didática acrescenta campos derivados, como prévia do `abstract`, rótulos, década e contagens de palavras e categorias.

As três tabelas longa e agregadas não são referenciadas pelos notebooks atuais. O histórico não inclui o script que selecionou as nove categorias nem a regra completa de amostragem; também não registra a URL e a data de aquisição da cópia intermediária. Os metadados remetem ao [arXiv](https://arxiv.org/), mas os direitos dos abstracts e artigos dependem de seus autores e licenças.

## Datasaurus — dependência remota

`encontro_5/datasaurus.ipynb` lê `datasaurus.csv` do repositório público [TidyTuesday de 13 de outubro de 2020](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-10-13). Não há cópia local. O notebook usa esses datasets para mostrar que resumos marginais semelhantes podem ocultar estruturas bidimensionais muito diferentes.

## Licenças

A licença MIT deste repositório cobre o material autoral, mas não se aplica automaticamente aos textos, metadados ou datasets de terceiros. Consulte a fonte e os termos próprios de cada conjunto antes de redistribuí-lo.
