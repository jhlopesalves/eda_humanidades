# Análise Exploratória de Dados e Inferência Estatística em Python

[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Feito para o Colab](https://img.shields.io/badge/Google%20Colab-pronto-orange.svg)](https://colab.research.google.com/)

Curso de introdução à programação em Python e à análise de dados para linguistas e pesquisadores das humanidades. São dois módulos de seis encontros semanais (2h cada), com notebooks executáveis, tarefas com gabarito comentado e dados reais: obras literárias, metadados bibliográficos e indicadores socioeconômicos.

O curso adota uma abordagem prática (*hands-on*): cada conceito é apresentado por meio de código executável, com incentivo à consulta da documentação oficial das bibliotecas utilizadas, da função `help()` e de fontes técnicas da comunidade, como o [Stack Overflow](https://stackoverflow.com/) e o [Cross Validated](https://stats.stackexchange.com/). Os notebooks são determinísticos, com sementes fixas, e podem ser reexecutados integralmente.

## Informações gerais

- **Instrutor:** Jhonatan H. Lopes
- **Local:** CAD 2, Laboratório B206 — Universidade Federal de Minas Gerais (UFMG)
- **Horário:** sextas-feiras, às 14h

## Como usar este repositório

**No Google Colab (recomendado):** clique no botão "Open in Colab" do encontro desejado na tabela abaixo. Nada precisa ser instalado — o notebook abre e roda no navegador.

**Localmente:** clone o repositório e instale as dependências:

```bash
git clone https://github.com/jhlopesalves/eda_humanidades.git
cd eda_humanidades
pip install numpy pandas matplotlib seaborn scipy statsmodels jupyter
```

## Módulo 1 — Python e estatística descritiva

| # | Encontro | Tópicos | Notebook | Tarefa |
| :-: | :--- | :--- | :-: | :-: |
| 1 | **Primeiros passos: Colab, Python e lógica** | Por que programação e análise de dados importam para as humanidades · por que Python · código aberto e cultura de software científico · notebooks e Google Colab | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_1/enc_1.ipynb) | [tarefa](./encontro_1/homework/enc_1_homework.ipynb) · [gabarito](./encontro_1/homework/enc_1_respostas_hw.ipynb) |
| 2 | **Fundamentos: listas, loops, condicionais e dicionários** | Variáveis e tipos · strings, listas, dicionários e conjuntos · indexação e fatiamento · condicionais e laços · funções, importações e módulos · objetos, atributos e métodos · leitura de erros e uso da documentação | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_2/enc_2.ipynb) | [tarefa](./encontro_2/homework/enc_2_homework.ipynb) · [gabarito](./encontro_2/homework/enc_2_respostas_hw.ipynb) |
| 3 | **Dicionários, métricas lexicais e funções** | Dicionários na prática · aprofundamento em laços · funções · métricas lexicais básicas aplicadas a obras integrais do Projeto Gutenberg | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_3/enc_3.ipynb) | [tarefa](./encontro_3/homework/enc_3_homework.ipynb) · [gabarito](./encontro_3/homework/enc_3_respostas_hw.ipynb) |
| 4 | **NumPy e pandas: do registro à tabela** | Arrays e vetorização · Series e DataFrame · leitura de CSV · seleção, filtragem e agrupamento (groupby) · Gapminder e Goodreads como estudos de caso | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_4/enc_4.ipynb) | [tarefa](./encontro_4/homework/enc_4_homework.ipynb) · [gabarito](./encontro_4/homework/enc_4_respostas_hw.ipynb) |
| 5 | **Estatística descritiva e visualização** | Medidas de tendência central e dispersão · histogramas e ECDFs · matplotlib e seaborn · por que visualizar antes de resumir (material extra: [datasaurus.ipynb](./encontro_5/datasaurus.ipynb)) · metadados do arXiv como estudo de caso | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_5/enc_5.ipynb) | — |
| 6 | **Forma, normalidade e dispersão** | Assimetria e forma das distribuições · gráficos Q-Q e normalidade · distribuição de Poisson vs. dados reais · entropia de Shannon | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_6/enc_6.ipynb) | — |

## Módulo 2 — da descritiva à inferência (em preparação)

O segundo módulo fecha os tópicos finais da estatística descritiva (correlação, transformações, normalização) e avança para a inferência estatística: amostragem, intervalos de confiança, testes de hipótese e modelos de regressão — sempre com exemplos linguísticos. Cronograma e notebooks serão publicados aqui.

## Dados

| Pasta | Conjunto | Fonte |
| :--- | :--- | :--- |
| `encontro_3/data/` | Cinco obras integrais em texto plano (Machado de Assis, Dostoiévski, Shakespeare, entre outras) | [Project Gutenberg](https://www.gutenberg.org/) (domínio público) |
| `encontro_4/data/` | Indicadores socioeconômicos por país (`gapminderDataFiveYear.csv`) | [Gapminder](https://www.gapminder.org/) |
| `encontro_4/data/` | Amostra de metadados de livros (`goodreads.csv`) | Goodreads |
| `encontro_5/data/` | Recortes de metadados de artigos científicos | [arXiv](https://arxiv.org/) |

## Estrutura do repositório

```
eda_humanidades/
├── encontro_1/
│   ├── enc_1.ipynb
│   └── homework/
│       ├── enc_1_homework.ipynb
│       └── enc_1_respostas_hw.ipynb
├── encontro_2/            # mesma estrutura
├── encontro_3/
│   ├── data/              # textos do Projeto Gutenberg
│   ├── enc_3.ipynb
│   └── homework/
├── encontro_4/
│   ├── data/              # Gapminder e Goodreads
│   ├── enc_4.ipynb
│   └── homework/
├── encontro_5/
│   ├── data/              # metadados do arXiv
│   ├── datasaurus.ipynb   # material extra
│   └── enc_5.ipynb
├── encontro_6/
│   └── enc_6.ipynb
├── LICENSE
└── README.md
```

## Ferramentas

- **Linguagem:** Python 3
- **Manipulação de dados:** `numpy`, `pandas`
- **Visualização:** `matplotlib`, `seaborn`
- **Estatística:** `scipy.stats` (e `statsmodels` no material extra)
- **Ambiente:** Google Colab / Jupyter

## Licença

Distribuído sob a licença MIT — ver [LICENSE](./LICENSE). Os textos do Projeto Gutenberg estão em domínio público; os demais conjuntos de dados pertencem às suas respectivas fontes e são usados aqui para fins didáticos.
