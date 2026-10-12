---
title: "Dados e proveniência"
toc-depth: 2
---

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

O arquivo contém 1.704 observações por país e ano, de 1952 a 2007, com as colunas `country`, `year`, `pop`, `continent`, `lifeExp` e `gdpPercap`. Ele é usado na tarefa e no gabarito do Encontro 4 e nas duas partes do Encontro 8. Corresponde ao recorte clássico associado à [Gapminder Foundation](https://www.gapminder.org/data/).

O recorte de 2007 tem 142 países. Uma linha representa um país em um ano: análises que reúnem todos os anos incluem observações repetidas dos mesmos países. Os gráficos de 2007 e as matrizes com todos os anos não descrevem a mesma população de observações.

A URL original de aquisição, a data do download, eventuais transformações e a licença específica desta cópia não estão registradas.

## Metadados de livros — `encontro_4/data/goodreads.csv`

O arquivo contém metadados de livros e inclui a coluna derivada `publisher_family`. Ele permanece como material de apoio, mas não é lido pelos notebooks atuais. O histórico indica que o arquivo foi renomeado e ajustado, porém não preserva uma página-fonte confiável, a data de aquisição, um procedimento completo de transformação ou a licença.

## arXiv — `encontro_5/data/`

| Arquivo | Conteúdo e papel no curso |
| :--- | :--- |
| `arxiv_subset.csv` | Recorte intermediário de metadados de 2020–2025 |
| `arxiv_eda_papers.csv` | Amostra didática usada nos Encontros 5–8 e na tarefa do Encontro 7 |
| `arxiv_eda_categories_long.csv` | Forma longa das associações artigo–categoria |
| `arxiv_eda_category_year_counts.csv` | Contagens por ano e categoria primária |
| `arxiv_eda_year_counts.csv` | Contagens por ano e área de primeiro nível |

`arxiv_eda_papers.csv` contém 3.387 linhas e 16 colunas. Seus identificadores existem em `arxiv_subset.csv`, e `paper_id` deve ser tratado como string. A amostra didática acrescenta campos derivados, como prévia do `abstract`, rótulos, década e contagens de palavras e categorias. Essas contagens dependem das regras de preparação dos metadados.

O exemplo com o maior número de autores remete ao [LongCat-Flash](https://arxiv.org/abs/2509.01322). A lista inclui autoria coletiva: suas 182 entradas não correspondem necessariamente a 182 pessoas distintas.

As três tabelas longa e agregadas não são referenciadas pelos notebooks atuais. O histórico não inclui o script que selecionou as nove categorias nem a regra completa de amostragem; também não registra a URL e a data de aquisição da cópia intermediária. Os metadados remetem ao [arXiv](https://arxiv.org/), mas os direitos dos abstracts e artigos dependem de seus autores e licenças.

## Datasaurus — `encontro_5/data/datasaurus.csv`

O repositório contém uma cópia local de `datasaurus.csv`, com 1.846 pontos distribuídos em 13 conjuntos de 142 pontos. A fonte de download é o [TidyTuesday de 13 de outubro de 2020](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-10-13), que remete ao trabalho [Same Stats, Different Graphs](https://www.research.autodesk.com/publications/same-stats-different-graphs/) e ao Datasaurus de Alberto Cairo.

`encontro_5/datasaurus.ipynb` usa a cópia local quando disponível e mantém a URL de download como alternativa. Os conjuntos mostram que resumos marginais semelhantes podem ocultar estruturas bidimensionais muito diferentes. A data de aquisição desta cópia e uma licença específica do arquivo não estão registradas no repositório.

## Amostras — `encontro_9/homework/amostras.csv`

O arquivo contém 500 linhas e quatro colunas, `A`, `B`, `C` e `D`, usadas na tarefa do Encontro 9 como amostras de distribuições desconhecidas. O código de geração, os parâmetros e a semente aleatória não foram preservados. A inspeção das amostras não recupera essas informações com certeza.

## Construções verbais — `encontro_10/data/vpcs.csv`

Apesar da extensão `.csv`, este arquivo é separado por tabulações. Contém 397 linhas e as colunas `CASE`, `CONSTRUCTION` e `GIVENNESS`. O Encontro 10 recodifica `CONSTRUCTION` como uma variável binária: 247 casos de VPO e 150 de VOP.

A atribuição preservada no notebook é Peters (2001), *Given vs. new information influencing constituent ordering in the VPC*, via uma tabela de Gries (2023). A [tabela e a referência reproduzidas por Gries](https://www.stgries.info/research/2023_STG_IndRels_EncApplLing2.pdf) permitem conferir as contagens. A URL exata de aquisição do arquivo, sua data e seus termos específicos de redistribuição não estão registrados.

O arquivo não fornece identificadores de participantes ou de itens que permitam avaliar dependência entre observações. A simulação binomial e o bootstrap por linhas da aula pressupõem uma unidade de reamostragem adequada; essa adequação não é demonstrada pela simples existência da tabela.

## Decisão lexical — `encontro_10/data/lexdec.csv`

O arquivo tem 1.659 linhas e 28 colunas, incluindo `Subject`, `RT`, `Word`, `Frequency` e `Length`. Ele está preservado, mas não é lido pelas aulas ou atividades atuais. A origem, os termos de uso e as transformações não estão documentados nesta cópia. Em particular, o nome `RT` não basta para estabelecer a unidade nem a escala da medida.

## Textos e registros incorporados às aulas

O trecho sobre Robert K. Merton e a passagem sobre hipótese científica são atribuídos às respectivas páginas da Wikipédia no primeiro uso. O repositório não registra a revisão nem a data de consulta dessas páginas.

Os registros de obras usados para introduzir dicionários e DataFrames são ilustrativos. Contagens de tokens e tipos não são medições das obras citadas; títulos e anos simplificam informações editoriais. Não devem ser reutilizados como dados bibliográficos ou linguísticos observados.

Os textos e arquivos de apoio foram preservados. Ausência de uso nas aulas atuais não resolve lacunas de fonte, transformação ou licença.

## Licenças

A licença MIT deste repositório cobre o material autoral, mas não se aplica automaticamente aos textos, metadados ou datasets de terceiros. Consulte a fonte e os termos próprios de cada conjunto antes de redistribuí-lo.
