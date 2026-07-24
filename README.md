# Análise Exploratória de Dados para as Humanidades

[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](./LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Feito para o Colab](https://img.shields.io/badge/Google%20Colab-pronto-orange.svg)](https://colab.research.google.com/)

Material introdutório de programação em Python e análise exploratória de dados para linguistas e pesquisadores das humanidades. O Módulo 1 reúne seis encontros de duas horas, notebooks de aula, tarefas e gabaritos comentados.

O curso foi construído de forma incremental e preserva essa história. Em particular, o Encontro 5 terminou antes do previsto; por isso, o Encontro 6 começa repetindo as células correspondentes e marca explicitamente onde entra o conteúdo novo. Essa duplicação é intencional e permite abrir o segundo notebook de forma autônoma.

## Contexto da oferta registrada

- **Instrutor:** Jhonatan H. Lopes
- **Local:** CAD 2, Laboratório B206 — Universidade Federal de Minas Gerais (UFMG)
- **Horário:** sextas-feiras, às 14h

## Como usar

No Google Colab, clique no botão do encontro desejado na tabela abaixo. Os notebooks baixam alguns dados públicos durante a execução, portanto é necessário acesso à internet.

Para trabalhar localmente, recomenda-se Python 3.11 e um ambiente virtual:

```bash
git clone https://github.com/jhlopesalves/eda_humanidades.git
cd eda_humanidades
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

No Windows, a ativação equivalente no PowerShell é `.venv\Scripts\Activate.ps1`.

## Módulo 1 — Python e estatística descritiva

| # | Encontro | Tópicos | Notebook | Tarefa |
| :-: | :--- | :--- | :-: | :-: |
| 1 | **Primeiros passos: Colab, Python e lógica** | Por que programação e análise de dados importam para as humanidades · notebooks · tipos básicos · operadores e lógica | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_1/enc_1.ipynb) | [tarefa](./encontro_1/homework/enc_1_homework.ipynb) · [gabarito](./encontro_1/homework/enc_1_respostas_hw.ipynb) |
| 2 | **Coleções e fluxo de controle** | Strings, listas, dicionários e conjuntos · indexação · condicionais · laços · funções · leitura de erros | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_2/enc_2.ipynb) | [tarefa](./encontro_2/homework/enc_2_homework.ipynb) · [gabarito](./encontro_2/homework/enc_2_respostas_hw.ipynb) |
| 3 | **Textos, dicionários e funções** | Processamento textual básico · frequências · diversidade lexical · hápax legomena · limites de métricas lexicais simples | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_3/enc_3.ipynb) | [tarefa](./encontro_3/homework/enc_3_homework.ipynb) · [gabarito](./encontro_3/homework/enc_3_respostas_hw.ipynb) |
| 4 | **NumPy e pandas: do registro à tabela** | Arrays e vetorização · Series e DataFrame · leitura de CSV · seleção, filtragem e agrupamento | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_4/enc_4.ipynb) | [tarefa](./encontro_4/homework/enc_4_homework.ipynb) · [gabarito](./encontro_4/homework/enc_4_respostas_hw.ipynb) |
| 5 | **Estatística descritiva e visualização** | Tendência central e dispersão · histogramas e ECDFs · matplotlib e seaborn · metadados do arXiv | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_5/enc_5.ipynb) | [Datasaurus](./encontro_5/datasaurus.ipynb) |
| 6 | **Forma, normalidade e dispersão** | Assimetria · gráficos Q-Q · referência de Poisson · entropia de Shannon | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhlopesalves/eda_humanidades/blob/main/encontro_6/enc_6.ipynb) | — |

O Módulo 2, da descritiva à inferência, permanece em preparação; seus notebooks ainda não estão neste repositório.

## Dados e reprodutibilidade

Os notebooks usam textos literários, o recorte clássico do Gapminder, metadados bibliográficos e recortes do arXiv. A origem conhecida, o papel de cada arquivo e as lacunas de proveniência estão registrados em [DATASETS.md](./DATASETS.md). Não presuma que a licença MIT deste repositório se estenda aos dados.

As sementes aleatórias estão fixadas nos exemplos que usam simulação. Alguns notebooks leem arquivos pela URL da ramificação `main`; isso facilita o uso no Colab, mas a URL não é uma versão imutável. Para uma reprodução exata, use os arquivos do mesmo commit do notebook.

## Validação

O validador estrutural usa apenas a biblioteca-padrão:

```bash
python scripts/validate_notebooks.py
```

Após instalar `requirements.txt`, também é possível executar em memória os notebooks de aula e os gabaritos. Os notebooks de tarefa são verificados apenas quanto à estrutura e à sintaxe, pois contêm espaços destinados às respostas dos estudantes.

```bash
python scripts/validate_notebooks.py --execute
python scripts/validate_notebooks.py --links
```

A opção `--links` consulta a rede e pode acusar indisponibilidades temporárias de serviços externos. A automação do repositório executa a validação estrutural em Python 3.11.

## Estrutura

```text
eda_humanidades/
├── encontro_1/ ... encontro_4/
│   ├── enc_N.ipynb
│   └── homework/
│       ├── enc_N_homework.ipynb
│       └── enc_N_respostas_hw.ipynb
├── encontro_3/data/       # textos literários
├── encontro_4/data/       # Gapminder e metadados de livros
├── encontro_5/
│   ├── data/              # recortes e tabelas derivadas do arXiv
│   ├── datasaurus.ipynb   # material complementar
│   └── enc_5.ipynb
├── encontro_6/enc_6.ipynb
├── scripts/validate_notebooks.py
├── DATASETS.md
├── requirements.txt
├── LICENSE
└── README.md
```

## Licença

O código e o material autoral do curso são distribuídos sob a licença MIT; consulte [LICENSE](./LICENSE). Textos, imagens e conjuntos de dados de terceiros permanecem sujeitos aos termos de suas fontes. Consulte [DATASETS.md](./DATASETS.md) antes de redistribuí-los.
