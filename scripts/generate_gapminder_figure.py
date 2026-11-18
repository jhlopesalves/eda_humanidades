"""Gera as duas versões da figura editorial do Gapminder para o site."""

from io import StringIO
from pathlib import Path

import matplotlib as mpl
import pandas as pd
from matplotlib.colors import to_rgba
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.ticker import NullLocator
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "encontro_4/data/gapminderDataFiveYear.csv"
OUTPUT = ROOT / "assets/figures"
YEAR = 2007

CONTINENTS = {
    "Africa": "África",
    "Americas": "Américas",
    "Asia": "Ásia",
    "Europe": "Europa",
    "Oceania": "Oceania",
}
# As paletas variam também em luminosidade para distinguir os grupos quando
# a percepção de matizes é reduzida.
THEMES = {
    "claro": {
        "text": "#202124",
        "muted": "#525a66",
        "grid": "#dce1e8",
        "axis": "#87919f",
        "continents": ("#ad521d", "#37a471", "#2457c5", "#5f2d76", "#71788e"),
    },
    "escuro": {
        "text": "#e7e9ed",
        "muted": "#b2bac7",
        "grid": "#363d49",
        "axis": "#747e8d",
        "continents": ("#ffab72", "#55fcd5", "#91b3ff", "#b434ef", "#777b7e"),
    },
}


def plot_gapminder(data: pd.DataFrame, theme: str) -> Figure:
    """Desenha a dispersão para o recorte de 2007, com um ponto por país."""
    style = THEMES[theme]
    palette = dict(zip(CONTINENTS, style["continents"], strict=True))
    rho = spearmanr(data["gdpPercap"], data["lifeExp"]).statistic

    # Como no Seaborn, normalizamos linearmente em pontos². O mínimo positivo
    # mantém os países menos populosos visíveis. Eles são desenhados por último.
    ordered = data.sort_values("pop", ascending=False, kind="stable")
    population = ordered["pop"]
    fraction = (population - population.min()) / (population.max() - population.min())
    areas = 23 + (1313 - 23) * fraction

    width, height = 432, 340
    left, right, top, bottom = 36, 421, 86, 236
    fig = Figure(figsize=(width / 72, height / 72))
    ax = fig.add_axes(
        (
            left / width,
            1 - bottom / height,
            (right - left) / width,
            (bottom - top) / height,
        )
    )

    ax.scatter(
        ordered["gdpPercap"],
        ordered["lifeExp"],
        s=areas,
        facecolors=[to_rgba(palette[c], 0.66) for c in ordered["continent"]],
        edgecolors=[to_rgba(palette[c], 0.91) for c in ordered["continent"]],
        linewidths=0.65,
        zorder=3,
    )
    ax.set_xscale("log")
    ax.set_xlim(230, 68000)
    ax.set_ylim(36, 86)
    ax.set_xticks(
        [500, 1000, 5000, 10000, 50000],
        ["500", "1 mil", "5 mil", "10 mil", "50 mil"],
    )
    ax.set_yticks([40, 50, 60, 70, 80])
    ax.xaxis.set_minor_locator(NullLocator())
    ax.tick_params(length=0, pad=7, labelsize=15, labelcolor=style["muted"])
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=style["grid"], linewidth=0.75)
    ax.spines[["top", "left", "right"]].set_visible(False)
    ax.spines["bottom"].set_color(style["axis"])
    ax.spines["bottom"].set_linewidth(0.75)

    # Um sistema de coordenadas em pontos mantém o alinhamento com as margens
    # do eixo quando o SVG inteiro é reduzido na página.
    def label(x, y, text, size=15, *, color=style["text"], **kwargs):
        return fig.text(x / width, 1 - y / height, text, fontsize=size, color=color, **kwargs)

    label(3, 31, "Renda e longevidade", 34, family="STIXGeneral")
    label(4, 54, f"{len(data)} países · {YEAR}", 15, color=style["muted"])
    label(427, 54, f"Spearman  ρ = {rho:.3f}".replace(".", ","), ha="right")
    label(4, top - 10, "Expectativa de vida (anos)")
    label(right, bottom + 44, "PIB per capita · escala logarítmica", ha="right")

    # Usa as mesmas cores de face e de contorno das marcas na área de dados.
    handles = [
        Line2D(
            [],
            [],
            marker="o",
            linestyle="none",
            markersize=7.6,
            markerfacecolor=to_rgba(palette[continent], 0.66),
            markeredgecolor=to_rgba(palette[continent], 0.91),
            markeredgewidth=0.65,
            label=name,
        )
        for continent, name in CONTINENTS.items()
    ]
    fig.legend(
        handles=handles,
        loc="center left",
        bbox_to_anchor=(4 / width, 1 - (bottom + 64) / height, 414 / width, 0),
        mode="expand",
        ncols=len(CONTINENTS),
        borderaxespad=0,
        borderpad=0,
        handlelength=0.8,
        handletextpad=0.4,
        fontsize=15,
        labelcolor=style["text"],
        frameon=False,
    )
    label(4, height - 11, "Área dos círculos: população", 14, color=style["muted"])
    label(427, height - 11, "Fonte: Gapminder", 13, color=style["muted"], ha="right")
    return fig


def main() -> None:
    """Lê o CSV do curso e exporta os SVGs sem depender do tema do sistema."""
    data = pd.read_csv(DATASET)
    data = data.loc[data["year"] == YEAR]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    # As fontes acompanham o Matplotlib. Traçados e IDs estáveis dispensam
    # fontes externas e permitem comparar duas gerações do mesmo ativo.
    with mpl.rc_context(
        dict(mpl.rcParamsDefault)
        | {
            "font.family": "DejaVu Sans",
            "svg.fonttype": "path",
            "svg.hashsalt": "gapminder-2007",
        }
    ):
        for theme in THEMES:
            figure = plot_gapminder(data, theme)
            svg = StringIO()
            figure.savefig(
                svg,
                format="svg",
                transparent=True,
                metadata={"Title": "Renda e longevidade", "Date": None},
            )
            # O backend SVG separa comandos de traçado por espaços e quebras
            # de linha. Mantemos as quebras e removemos os espaços finais.
            content = "\n".join(line.rstrip() for line in svg.getvalue().splitlines())
            (OUTPUT / f"gapminder-2007-{theme}.svg").write_text(content + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
