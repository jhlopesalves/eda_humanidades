# Course publication review

Reviewed on 12 October 2026, on branch `polish-course`, starting at `f5142254cbf3d70470a3fafdf5afe11815aab372`.

The review covers the twelve lesson notebooks for Encontros 1–10, including Datasaurus and Encontro 8, parte 2. All 547 original cells were inspected. During the content revision, 457 original cell sources were deliberately left unchanged. Existing edits in Encontros 1–3 were retained. The taught topics, their broad order, introductory loops, substantive examples and methodological cautions were preserved.

## Commits and files

| Commit | Message | Scope |
| :--- | :--- | :--- |
| `e9b2977d9d9acd8aab501a8c5fdd250308d11df0` | `refactor(course): polish lesson notebooks and instructional content` | The twelve notebooks listed below |
| `01a1cfc3bdaf0cbd0c1e71923964c4375124ff20` | `feat(site): improve Quarto lesson structure and presentation` | The same twelve notebooks and `_quarto.yml` |
| Third commit | `chore(site): refine documentation, styling, and project metadata` | `index.qmd`, `about.qmd`, `_quarto.yml`, `styles.css`, `README.md`, `DATASETS.md`, `.github/workflows/publish.yml`, `requirements-notebooks.txt`, `scripts/check_course.py`, this document |

The third commit contains this document, so its identifier is reported in the handover rather than recorded inside itself.

The lesson files changed in both of the first two commits are:

```text
encontro_1/enc_1.ipynb
encontro_2/enc_2.ipynb
encontro_3/enc_3.ipynb
encontro_4/enc_4.ipynb
encontro_5/datasaurus.ipynb
encontro_5/enc_5.ipynb
encontro_6/enc_6.ipynb
encontro_7/enc_7.ipynb
encontro_8/enc_8.ipynb
encontro_8/enc_8-parte2.ipynb
encontro_9/enc_9.ipynb
encontro_10/enc_10.ipynb
```

No homework, answer key, dataset, portrait or licence file was edited. SHA-256 comparisons with the initial working copies confirmed that all 29 such files were unchanged; `.gitignore` was also unchanged. No assets or apparently unused data were deleted.

## Lesson corrections

| Lesson | Main corrections and editorial decisions |
| :--- | :--- |
| 1 | Repaired Markdown fences and kept the heading demonstration out of the page outline. Distinguished notebook contents from runtime state and year subtraction from exact age. Qualified the mean's domain. Preserved basic Python examples and documentation inspection. |
| 2 | Kept the deliberate `KeyError` and the progression through `.get()`, a textual default and a substantively justified zero default. Explained nested indexing and attributed the hypothesis passage. Retained introductory loops and dictionary updates. |
| 3 | Corrected the finite, non-empty TTR bounds to `1/N <= TTR <= 1`, with length and preprocessing cautions. Corrected the claim about accented identifiers. Retained the simple preprocessing attempt, its limitation, explicit frequency loop, `.get()` version and equality check. |
| 4 | Identified invented word counts as illustrative and qualified publication-year simplifications. Updated the explanation of string dtypes for the executed pandas version and clarified how missing values affect counts. |
| 5 | Attributed the arXiv data before use. Made data loading prefer the local copy while retaining the Colab URL. Stated the domain of sample variance/SD and the ECDF. |
| Datasaurus | Preserved the numerical setup, Cohen's d and delayed graphical reveal. Gave the immediate debrief, second pair, corpus argument and final workflow distinct jobs. Removed repeated conclusions while keeping the criticism of inappropriate scalar comparisons and its literature grounding. |
| 6 | Clarified the scope of `dropna()`, categorical missingness and entropy. Empty input now raises `ValueError`; one observed category has zero entropy. Qualified the Poisson reference as a comparison, not a model adequacy test. |
| 7 | Added orientation and a conclusion around the existing scatterplot/pairplot progression. Qualified the extreme author count: 182 entries include collective authorship. Retained the full author-list demonstration. |
| 8 | Distinguished calculation of a descriptive coefficient from assumptions used in inference. Clarified Spearman's relation to Pearson on ranks and qualified correlation diagonals. Distinguished pooled country-year data from the 2007 cross-section. |
| 8, parte 2 | Repaired the `.loc` explanation and displayed figure adjustments explicitly. Passed the intended `Axes` to `despine()`. Restored the population legend alongside the continent legend. Clarified that marker area represents population but does not weight the correlation. Retained the progressive construction of the graphic. |
| 9 | Distinguished continuous density from probability at an exact point, parameters from sample statistics, variance from SD, and the model CDF from the empirical CDF. Set `common_norm=False` so group KDEs match the explanation of separate unit areas. |
| 10 | Validated binary labels before recoding the tab-separated VPC data. Stated the independent, common-probability assumptions of the binomial demonstration. Distinguished SE, bias and dependence; explained replacement and the resampling unit. Clarified percentile/BCa intervals and frequentist coverage. |

The statistical corrections were checked against the relevant primary documentation, including [Python's string constants](https://docs.python.org/3/library/string.html), [Seaborn's KDE normalisation](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) and [SciPy's bootstrap methods](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html).

Datasaurus retains both protected methodological statements. The corpus-linguistics thesis remains visible without opening a disclosure; only supporting Deviation of Proportions detail is collapsed. Its numerical demonstrations still precede the Dino/Star plots. Inline math delimiters in Encontros 5, 6 and 8, parte 2 were repaired for both notebook and Quarto rendering; mathematical notation was removed from the Cohen's d heading to keep the TOC readable. Section 5.1 is now **“Limites dos resumos numéricos”**. Other formulaic “from X to Y” headings were removed.

## Website presentation

Raw first-cell YAML supplies a descriptive browser title through `pagetitle`, without duplicating the H1 or exposing YAML as prose in the website. The source H1 remains readable in Jupyter and Colab. Preliminary recaps are unnumbered, substantive sections have clearer hierarchy, and existing activities are linked at lesson endings.

The Colab image description is “Abrir no Google Colab”. Every lesson explains that the static pages show saved results. Imports, helpers and some supporting constructions are folded; beginner algorithms remain visible. Long inspection outputs are constrained to 24 rem and can be scrolled. All 41 plotted figures have captions and meaningful alternative descriptions.

Encontros 7–10 and both parts of Encontro 8 were rendered before being added to the render list and sidebar. They are included in the complete local build and the previous/next sequence. This branch has not been deployed.

The homepage has no on-page TOC, “Materiais” heading or resource cards. It provides a clear starting link, compact instructor credit and the actual encounter sequence. Both module lists use the same spacing; “Parte 2: visualização” uses the interlude's indented treatment. The full biography, social links and project acknowledgement are on `about.qmd`; provenance and the existing MIT licence are linked quietly in the footer.

The site retains the Cosmo/Darkly themes. CSS removes the old icon override and card styles, uses theme-specific link/muted colours, supplies visible keyboard focus, constrains long outputs and allows tables and mathematics to scroll locally. Inline filenames wrap in headings and prose tables. Heading code uses the surrounding foreground without an incompatible background. Previous/next links and disclosure labels were corrected after the dark theme measured only 3.39:1 contrast. Current-page breadcrumbs, a few syntax tokens, captions, blockquotes and saved ANSI traceback colours also needed contrast corrections. The traceback text and its emphasis are preserved, with the theme foreground replacing stored inline colours. Native Quarto controls provide navigation and colour switching; no new site JavaScript or frontend dependency was added.

The workflow pins Quarto 1.10.18, the version used locally, using the action's [documented version input](https://github.com/quarto-dev/quarto-actions/tree/main/setup). `execute.enabled: false` is retained: publishing saved outputs and executing notebook code remain separate operations.

## Verification

The local Python environment uses Python 3.14.7. Its direct notebook and checking dependencies are recorded in `requirements-notebooks.txt`; `README.md` gives uv and Quarto commands. `scripts/check_course.py` checks notebook format and saved execution counts, optionally executes fresh kernels without rewriting sources, and checks the rendered pages and local targets.

All twelve notebooks executed in fresh kernels, covering 252 code cells. There was one expected, tagged `KeyError` in Encontro 2 and no unexpected notebook error or cell stderr output. Numerical checks cover independent frequency/median implementations, TTR bounds, variance/SD against NumPy, entropy edge cases, Pearson on ranks against Spearman, the 142-country cross-section, the normal CDF, and binomial/bootstrap quantities for 247 VPO observations out of 397. The repaired two-legend graphic was executed again and inspected in the browser.

The complete site renders 15 pages without Quarto warnings. Source and render checks cover one H1 per page, human browser titles, Portuguese Colab descriptions, saved-output notes, all 41 plot descriptions/captions, and 4,064 local links, resources and fragment targets.

Browser review uses the actual Chrome extension browser and a local preview. All encounters, the homepage, provenance and about page were inspected. Checks include the sidebar, TOCs, previous/next links, code disclosure, long outputs, captions, attribution, light/dark themes and narrow layouts. Each of the 15 pages was checked at 375 × 812 and 1440 × 900 in both themes: 60 page/theme/viewport combinations, with no page-level horizontal overflow or sampled text contrast failure. The minimum measured contrast was 4.54:1. Additional tablet inspections used 768 × 1024. Native code disclosure responded to Enter with a visible focus outline; the long heatmap help output scrolled by keyboard. Both protected Datasaurus statements were outside collapsed content. The two-legend Gapminder figure and rendered binomial notation were inspected visually. These measurements cover DOM text and local layouts; they are not a complete assistive-technology assessment.

External checking returned 200/206 for 44 of 47 distinct lesson/site URLs. Three sites restricted automated access: Stack Overflow returned 403, Cambridge returned 429, and LinkedIn returned 999. Those responses do not establish that the links are broken. Colab routes returned 200; that checks route availability, not interactive execution inside Colab. Their links continue to target `main`, so the unpushed branch's revisions are not yet available there.

## Limits and deferred decisions

The kernel launcher prints its local TCP transport warning outside the notebook outputs. This is an environment notice; it does not appear in the rendered lessons. No kernel transport configuration was changed as part of this course edit.

Some source/download dates, selection and preprocessing scripts, data-generation parameters and third-party terms remain unavailable. These gaps are documented in `DATASETS.md`; they were not replaced with guessed information. Direct dependency pins do not capture every transitive dependency or guarantee identical results on other platforms.

No new syllabus, future meeting schedule, homework redesign, author credential, grant identifier, citation identifier or separate prose licence was invented. The existing MIT licence was preserved. Changing that licence or resolving third-party redistribution terms would require a separate decision and supporting source information. The raw and apparently unused data remain intact.

There was no remote CI/deployment run. No PR was opened, no branch was merged and nothing was pushed. The final handover records the three commit identifiers and the clean working tree.
