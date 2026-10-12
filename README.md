# Estatística Descritiva e Inferencial em Python para Humanidades

Curso de programação, análise de dados e estatística em Python voltado a estudantes e pesquisadores das humanidades. Os materiais combinam fundamentos de Python, análise exploratória, visualização e raciocínio estatístico com exemplos baseados em textos, metadados bibliográficos e dados socioeconômicos.

**[Acessar o site do curso](https://jhlopesalves.github.io/eda_humanidades/)** · **[Começar pelo Encontro 1](https://jhlopesalves.github.io/eda_humanidades/encontro_1/enc_1.html)**

## Sobre o curso

O curso foi desenvolvido para que programação e estatística sejam aprendidas em conjunto. O código não aparece apenas como ferramenta para produzir resultados: ele também permite examinar como medidas, gráficos e procedimentos estatísticos são construídos, quais decisões entram em uma análise e como os resultados podem ser interpretados.

Os notebooks formam a fonte principal das aulas. O site publica o conteúdo em formato de leitura; no início de cada encontro há um link para abrir o respectivo notebook no Google Colab e executar ou modificar os exemplos.

## Conteúdo

### Módulo 1 — Python e estatística descritiva

1. [Primeiros passos: Colab, Python e lógica](encontro_1/enc_1.ipynb)
2. [Fundamentos de Python: listas, loops, condicionais e dicionários](encontro_2/enc_2.ipynb)
3. [Funções e métricas lexicais](encontro_3/enc_3.ipynb)
4. [NumPy e pandas](encontro_4/enc_4.ipynb)
   - [Interlúdio: Datasaurus Dozen](encontro_5/datasaurus.ipynb)
5. [Estatística descritiva e visualização](encontro_5/enc_5.ipynb)
6. [Forma, normalidade e dispersão](encontro_6/enc_6.ipynb)

### Módulo 2 — Associação, probabilidade e inferência

7. [Relações entre variáveis](encontro_7/enc_7.ipynb)
8. [Correlação e associação](encontro_8/enc_8.ipynb)
   - [Parte 2: visualização](encontro_8/enc_8-parte2.ipynb)
9. [Distribuição normal](encontro_9/enc_9.ipynb)
10. [Amostragem e incerteza](encontro_10/enc_10.ipynb)

## Como usar os materiais

Para leitura, utilize preferencialmente o **site do curso**, que organiza os encontros em sequência e apresenta o código junto às saídas salvas.

Para executar os exemplos, abra o encontro desejado e use o link **Abrir no Google Colab** disponível no início da aula.

Este repositório reúne os notebooks-fonte, atividades, gabaritos, conjuntos de dados usados no curso e os arquivos necessários para publicar o site.

## Equipe e projeto

**Instrutor e responsável pelos materiais:** Jhonatan H. Lopes  
**Coordenação do projeto:** Deise Prina Dutra

Curso desenvolvido no âmbito de um projeto da **Faculdade de Letras da Universidade Federal de Minas Gerais (UFMG)**, com apoio da **FAPEMIG — APQ-01173-22**.

## Dados e proveniência

As fontes conhecidas dos conjuntos de dados, transformações identificáveis e lacunas de documentação estão registradas em [Dados e proveniência](DATASETS.md).

Quando o histórico do projeto não permite reconstruir com segurança a origem, a transformação ou os termos de um arquivo, essa limitação é registrada explicitamente em vez de ser preenchida por suposição.

## Licença

Consulte [LICENSE](LICENSE) para a licença atualmente adotada pelo repositório.

Textos, imagens, metadados e conjuntos de dados de terceiros permanecem sujeitos aos termos de suas respectivas fontes; a presença de um arquivo neste repositório não o relicencia. Consulte também [Dados e proveniência](DATASETS.md).

## Desenvolvimento do site

O site é gerado com [Quarto](https://quarto.org/) e publicado pelo GitHub Pages.

Para pré-visualizar localmente, com Quarto instalado:

```bash
quarto preview
```

A publicação usa as saídas já salvas nos notebooks; o processo de renderização do site não reexecuta automaticamente as aulas.
