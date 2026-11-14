# Audit report: scientific, technical and editorial review

Branch `audit/scientific-quality-review`, based on `main` at
`6a9d209502b622e11a0c319fb381a696bb9dad27` (2026-11-12, “MAINT: Ajustes no
heatmap encontro 8.”). The working tree was clean when the branch was created.

This report records the evidence first and the corrections second. The
inventory below was committed **before** any notebook, script or document was
changed; the “Final status” fields were filled in after implementation.

## 1. Method and environment

| Step | What was done |
|---|---|
| Saved-state check | `scripts/check_course.py` (no flags) on `main`, then on each notebook separately. |
| Fresh execution | Every lesson notebook and every answer key executed top to bottom in a new kernel, with the lesson directory as working directory. The executed copies were written to a scratch directory, never over the sources. |
| Output comparison | Saved outputs compared with fresh outputs cell by cell: text exactly; PNG figures by pixel difference. |
| Encontro 12 | Executed in a separate, temporary environment (Python 3.13, spaCy 3.8.18, `pt_core_news_sm` 3.8.0, scikit-learn 1.9.1, statsmodels 0.15.0, pyarrow), because these packages are not part of `scripts/requirements.txt`. Extra cells computed PCA loadings and pooled statistics. Nothing from that environment was saved into the notebook. |
| Rendering | `quarto render` (Quarto 1.10.18, the CI version) on `main` and on a scratch copy. |
| Site check | `check_site()` from `scripts/check_course.py` on each rendered page. |
| Figures | The saved PNGs of the substantive figures in encontros 7–12 were viewed directly, not only their code. |
| Independent recalculation | Exact hypergeometric p-value (encontro 11), Spearman matrices and quoted values (encontro 8), Holm adjustment and PCA loadings (encontro 12), checksums of the pinned data URLs (encontro 10, part 2). |

Course environment: `.venv`, Python 3.14.7, with every package pinned in
`scripts/requirements.txt` installed at the pinned version (numpy 2.5.4,
pandas 3.0.6, matplotlib 3.11.2, seaborn 0.13.2, scipy 1.18.1, nbclient 0.11.0,
nbformat 5.11.1). pyarrow, spaCy, scikit-learn, statsmodels and NLTK are
**not** installed there.

Classification used below: **mathematical** error, **methodological**
problem, **interpretative** problem, or **reasonable alternative** (not an
error). Field “Status” is the assessment before any change; “Final status” is
the outcome.

## 2. Baseline results on `main`

| Check | Result |
|---|---|
| `quarto render` | **Fails**: `ERROR: Cell label names must be unique (found duplicate '#fig-autores-abstract-log')` in `encontro_7/enc_7.ipynb`. |
| GitHub Actions “Publicar site Quarto no GitHub Pages” | The last three runs on `main` (2026-11-12) **failed** at the render step. The published site is therefore still the build of 2026-10-30. |
| `scripts/check_course.py` (saved state) | Stops at `encontro_7/enc_7.ipynb`: execution counts `[…, 12, 14, 13, 16]`. Per notebook: enc_7 and enc_10-parte2 fail; every other configured notebook passes. Unpublished enc_11, enc_12 and the final project also fail (never executed in order). |
| Fresh execution, configured notebooks | All execute without unexpected errors; the only error is the intentional, tagged `KeyError: 'preposição'` in encontro 2. |
| Fresh vs saved outputs | **Identical** in enc_1, 2, 3, 9, 10 and 10-parte2 (except pandas `memory usage` lines). The other differences are environmental: object addresses in `Styler` reprs, pandas `memory usage`, figure sizes differing by 1 px, Python's `help()` formatting in answer keys. Substantive exceptions: enc_7 (saved with pandas 2.x in Colab) and enc_8, cell 20 (order of tied rows). See below. |
| Site check (after unblocking the render in a scratch copy) | Fails for enc_7 and enc_8: “missing Portuguese Colab description”. All other pages pass. |
| `check_course.py --execute` | Cannot pass for enc_8: its assertion `len(gapminder_2007) == 142` refers to a variable that no longer exists in that notebook (see R-02). |

## 3. Findings by encounter

### Encontros 1–6 and the Datasaurus interlude

No defects were identified. All seven notebooks execute in a fresh kernel; their
saved outputs match the fresh outputs apart from the environmental differences
listed above. The independent assertions in `scripts/check_course.py` pass.
These lessons were checked computationally and spot-read; they were not
reviewed line by line, in line with the brief's instruction to avoid broad
rewrites of foundational material.

### Encontro 7 — `encontro_7/enc_7.ipynb`

Context: commit `13f09e2` (“MAIN: botão colab encontro 7”) was saved from
Google Colab (`metadata.colab.machine_shape = "hm"`, pandas 2.x outputs). It
rewrote the badge cell, added cell 25 and introduced leading blank lines into
several cells. An overwritten commit, `dd82113` (“MAIN: Ajustes nos
scatterplots do encontro 7”), shows that changes to the scatterplots were
intended. Cell 25 is therefore treated as deliberate content, not as an
accident.

#### E7-01 — Duplicate figure label breaks the site build
- **Location:** cell 25 (`dVducUysoiYO`), `#| label: fig-autores-abstract-log`; the same label already exists in cell 21 (`k4bWAFB5yyZR`).
- **Severity / class / status:** blocker · publication · verified defect.
- **Evidence:** `quarto render` aborts with the duplicate-label error; GitHub Actions runs 43309992034, 43310099341 and 43313117822 failed. In a scratch copy, renaming only this label lets the whole site render (exit 0).
- **Consequence:** nothing can be published from `main`, including fixes to other lessons.
- **Proposed correction:** give cell 25 a unique label, `fig-autores-abstract-log-comparacao`. Keep the cell.
- **Verification:** `quarto render` exits 0, and the page contains both figure IDs.
- **Final status:** *pending*.

#### E7-02 — Quarto options ignored in cells that begin with a blank line
- **Location:** cells 3 (`218040c3`), 10 (`hL90LTkRyYr-`) and 27 (`QvatqeEio0wE`).
- **Severity / class / status:** high · publication/graphical · verified defect.
- **Evidence:** in the rendered page, the `#|` lines appear as literal comments in the code. The imports are not folded, and figures `fig-autores-abstract-inicial` and `fig-autores-abstract-log-marcas` have no ID, caption or alt text (`grep` of the rendered HTML).
- **Consequence:** two figures lose their caption and alt text (an accessibility regression), and the cross-reference targets disappear.
- **Proposed correction:** remove the leading blank line. This does not change any Python code.
- **Verification:** the figure IDs are present in the HTML, and the site check counts captions for the plots.
- **Final status:** *pending*.

#### E7-03 — Colab badge lost its Portuguese description and runtime note
- **Location:** cell 0 (no `id`).
- **Severity / class / status:** high · publication · verified defect.
- **Evidence:** before `13f09e2`, the cell had `alt="Abrir no Google Colab"` and `<p class="lesson-runtime-note">…</p>`. Now it has `alt="Open In Colab"` and no note. The site check fails on this page. The cell also lacks the `id` that nbformat 4.5 requires (`MissingIDFieldWarning`).
- **Proposed correction:** restore the previous badge text and note verbatim, and add a stable cell `id`.
- **Verification:** the site check passes for the page, and `nbformat.validate` gives no warning.
- **Final status:** *pending*.

#### E7-04 — Saved outputs not produced in order, nor in the documented environment
- **Location:** whole notebook. Execution counts `1…12, 14, 13, 16`: cell 25 (count 14) ran after cell 26 (count 13), and count 15 is missing. `info()` output shows `pandas.core.frame.DataFrame` and `object` columns (pandas 2.x), while the course pins pandas 3.0.6.
- **Severity / class / status:** high · reproducibility · verified defect.
- **Evidence:** saved-state check failure; comparison with fresh execution.
- **Consequence:** the saved outputs cannot be shown to correspond to an in-order run of the current code.
- **Proposed correction:** re-execute the notebook from a clean kernel in the documented environment and keep the fresh outputs. Pearson r = 0.084 and every other number must stay the same.
- **Verification:** saved-state check, fresh-vs-saved comparison of the text outputs, visual inspection of the figures.
- **Final status:** *pending*.

#### E7-05 — Unavailable font weight emits a warning in the documented environment
- **Location:** cell 27, `fontweight="semibold"`.
- **Severity / class / status:** low · graphical/reproducibility · verified defect.
- **Evidence:** fresh execution writes `findfont: Failed to find font weight semibold for DejaVu Sans, now using 700.` to stderr. Saved into the notebook, that line would be published on the page.
- **Proposed correction:** use `"bold"` (weight 700). Matplotlib already substitutes it, so the rendered figure is unchanged.
- **Final status:** *pending*.

#### E7-06 — Axis label contradicts the lesson's own definition of the variable
- **Location:** cell 26 (`uJQuJfvrypyP`): title “Número de autores e comprimento do abstract”, x-label “Número de autores”.
- **Severity / class / status:** low · pedagogical · verified defect.
- **Evidence:** cells 9, 13 and 16 insist that `n_authors` counts *entries* in the authorship field (collective authorship included), not people. All other figures say “entradas de autoria”.
- **Proposed correction:** “Entradas de autoria e comprimento do abstract” and “Entradas de autoria por artigo”.
- **Final status:** *pending*.

#### E7-07 — “As duas vistas abaixo” now contains three figures
- **Location:** cell 24 (`publication-scale-comparison`) opens a `layout-ncol=2` block that now holds cells 25, 26 and 27.
- **Severity / class / status:** low · pedagogical · requires authorial decision.
- **Evidence:** the text announces a linear and a logarithmic view; cell 25 adds a second logarithmic view.
- **Proposed correction:** none applied. Whether cell 25 should stay inside the comparison, move before it, or replace cell 21 is a decision for the author.
- **Final status:** *pending*.

Scientific content: verified and retained. The sample-paper coordinates in
cell 8 match the data (2001.04171 → (2, 108); 2001.04417 → (3, 170)). The
log-distance table in cell 22 is correct (log₁₀ 1.784 ≈ 0.251), and so are
Pearson r = 0.084 and the inverse transformation.

### Encontro 8 — `encontro_8/enc_8.ipynb`

#### E8-01 — Quarto options ignored in cells that begin with a blank line
- **Location:** cells 35 (`d8d2d170`), 38 (`1ab019f6`) and 42 (`3f909520`).
- **Severity / class / status:** high · publication/graphical · verified defect.
- **Evidence:** in the rendered page, `fig-arxiv-spearman` and `fig-gapminder-spearman` have no ID, caption or alt text, and the Gapminder preparation code is not folded.
- **Proposed correction:** same as E7-02. No re-execution is needed, because the Python code is unchanged.
- **Final status:** *pending*.

#### E8-02 — Colab badge lost its Portuguese description and runtime note
- **Location:** cell 0 (no `id`).
- **Severity / class / status:** high · publication · verified defect. Same evidence and correction as E7-03; the site check fails on this page.
- **Final status:** *pending*.

#### E8-03 — Order of tied rows is not reproducible
- **Location:** cell 20 (`e7e6ac92`), `sort_values(by="n_authors", ascending=False)`.
- **Severity / class / status:** low · reproducibility · verified, retained.
- **Evidence:** the two articles with 33 entries (rows 1349 and 1655) appear in a different order in the fresh run. Their ranks (3383.5) and the explanation in cell 21 are unaffected.
- **Proposed correction:** none. This is display order only; `kind="stable"` would remove the variation if the author wants it.
- **Final status:** *pending*.

Scientific content: verified and retained. The quoted values were recalculated
independently: the arXiv Spearman submatrix (0.050 / 0.111 / 0.154),
categories × title −0.124, and Gapminder ρ(gdpPercap, lifeExp) = 0.826,
ρ(year, lifeExp) = 0.446, ρ(year, gdpPercap) = 0.227, with 1,704 rows. The
explanation of pooled country-year correlations correctly separates
between-country and within-country variation, and makes no inferential
claims about the 1,704 dependent rows.

### Encontro 8, part 2 — `encontro_8/enc_8-parte2.ipynb`

No defects identified; retained unchanged, as the brief requires. Every saved
output matches a fresh run (the only difference is the memory address of a
function printed by `%whos`). The independent assertions in
`check_course.py` pass.

### Encontro 9 — `encontro_9/enc_9.ipynb`

No defects identified. Saved outputs match a fresh run exactly. The
statements about density, area, P(X = x) = 0, the N(μ, σ²) notation versus
NumPy's `scale` argument, and the KDE, ECDF and Q–Q readings are correct.

### Encontro 10 — `encontro_10/enc_10.ipynb`

Saved outputs match a fresh run exactly, including the BCa interval
[0.574, 0.670] and every standard error.

#### E10-01 — Histograms of p̂ use bins that do not match its discrete support
- **Location:** cell 38 (`fig-proporcoes-simuladas`) and cell 63 (`fig-bootstrap-percentil`), both `bins="fd"`. The notebook has no cell IDs (nbformat 4.0).
- **Severity / class / status:** medium · graphical · verified defect.
- **Evidence:** p̂ and p̂* take only the values k/397, so they are 1/397 ≈ 0.00252 apart. The Freedman–Diaconis width for these 5,000 values is about 0.0038, so each bin holds one *or* two possible values. The saved figure shows the resulting comb: neighbouring bars of about 400 and 175 (cell 38). The artificial multimodality has nothing to do with the binomial shape the lesson teaches.
- **Consequence:** the figure suggests a jagged, multimodal sampling distribution, which contradicts the text (“concentrado perto de 0,622”) and the binomial model introduced next.
- **Proposed correction:** use one bin per possible count k, with edges at (k ± 0.5)/n, plus one explanatory comment. Statistical content, labels and captions are unchanged. In cell 63, also move the legend to the empty upper-left area, where it no longer covers the data, and use white bar edges, as in cell 38.
- **Verification:** the revised figures were generated and inspected (prototype); all other outputs of the notebook stay byte-identical.
- **Final status:** *pending*.

#### E10-02 — `bootstrap_result` is reused for the percentile call and the BCa call
- **Location:** cell 55 (percentile) and cell 65 (BCa); cells 57, 59 and 63 read the first object.
- **Severity / class / status:** low · computational · optional improvement (reasonable alternative).
- **Evidence:** in order, every cell reads the intended object. If cell 63 is re-run after cell 65, it plots the BCa call's resamples. That is still a valid bootstrap distribution, and its limits are recomputed with `np.quantile`, so the figure stays correct but its draws change. The validator's assertions refer to the final (BCa) object.
- **Proposed correction:** optional rename (`percentile_bootstrap_result`). Deferred to avoid churn in a correct lesson.
- **Final status:** *pending*.

Verified and retained: the Bernoulli/binomial derivations, SE = √(p(1−p)/n),
the exact equivalence between the bootstrap of 0/1 data and Binomial(n, p̂)/n,
the `ddof=1` convention of `standard_error`, the coverage schematic (19 of 20
intervals contain 0.60), and the interpretation of the confidence interval.

### Encontro 10, part 2 — `encontro_10/enc_10-parte2.ipynb`

All numerical outputs match a fresh run exactly, including the out-of-order
cell (E10b-02). Units of analysis are handled correctly: participant summaries
with equal weight per person; word-level pairs resampled as complete rows;
trial-weighted means reconstructed exactly from cluster sums and counts in the
cluster bootstraps. The empirical SE formula s/√n·√((n−1)/n), the
odd-n argument for the median, and the interpretation of all three resampling
schemes are correct.

#### E10b-01 — The code does not do what the text describes when reading data
- **Location:** cell 7 (`fb34f876`) says the data are read from `data/lexdec.csv`, then from `encontro_10/data/lexdec.csv`, and only then from a fixed URL. Cells 8 (`e484d536`) and 12 (`QPcPLQPjpE6q`) read **only** from commit-pinned GitHub URLs.
- **Severity / class / status:** medium · reproducibility/pedagogical · verified defect.
- **Evidence:** the source code. The pinned `lexdec.csv` (commit `0c047c1`) has the same SHA-256 as the local file. The pinned `lexdec_colunas.csv` (commit `97b1ab8`) differs only in line endings (CRLF in the working tree), and the parsed tables are identical.
- **Consequence:** the notebook cannot be validated offline (in CI or locally without a network), and the text misdescribes the code.
- **Proposed correction:** implement the local-first reading that the text describes, with the same pinned URL as fallback. Apply the same pattern to the glossary.
- **Verification:** fresh execution produces identical outputs.
- **Final status:** *pending*.

#### E10b-02 — One saved execution count out of sequence
- **Location:** cell 67 (`eac9f734`), count 67 between counts 32 and 34.
- **Severity / class / status:** medium · reproducibility · verified defect (counter only).
- **Evidence:** a fresh in-order run reproduces this cell's printed summary character for character, and every other output in the notebook.
- **Proposed correction:** after the verified in-order run, record that run's execution counts. The outputs, which were verified identical, stay byte-for-byte unchanged.
- **Final status:** *pending*.

#### E10b-03 — Minor wording: “percentual” for “percentil”
- **Location:** cell 76 (`f88aaaf7`, code comment) and cell 111 (`c835ee6b`, code comment).
- **Severity / class / status:** low · pedagogical · verified defect. Deferred, because both are code comments and the fix would mean re-touching executed cells for a cosmetic gain.
- **Final status:** *pending*.

### Encontro 11 — `encontro_11/enc_11.ipynb` (not published)

The statistics are sound. The permutation p-value (0.0888, from 10,000
resamples; Monte Carlo SE ≈ 0.003) agrees with the **exact** permutation
p-value under the same rule (doubling the smaller tail): 0.0847, from the
hypergeometric distribution of clicks in “creature” given 50 clicks in 4,105
impressions. The two-sided Fisher exact test gives 0.066; it uses a different
tail convention, which is not an error. The identity δ = p₁ − p₂ for Cliff's
delta on binary outcomes holds both for the population quantity and for the
sample estimator. The Cohen's d base-rate demonstration is arithmetically
correct (0.056 / 0.021 / 0.013).

#### E11-01 — Never executed in a recorded order
- **Location:** all 26 code cells have `execution_count: null`, but outputs are saved.
- **Severity / class / status:** blocker (publication) · reproducibility · verified defect.
- **Evidence:** saved-state check. A fresh run in the course environment succeeds and reproduces every saved number, **except** cell 26 (`6bXHkAlkphSL`): 0.52 saved, 0.60 fresh, because of E11-02.
- **Proposed correction:** execute from a clean kernel once E11-02 to E11-05 are settled. Deferred.
- **Final status:** *pending*.

#### E11-02 — Unseeded generator in a published demonstration
- **Location:** cell 3 (`cdbd079f`), `coin_rng = np.random.default_rng()`.
- **Severity / class / status:** medium · reproducibility · requires authorial decision.
- **Evidence:** the saved outputs of cells 24–26 (“coroa”, 0.52) cannot be reproduced. The cell that appends flips one at a time is meant to be re-run interactively; a seed would not stop that.
- **Proposed correction:** seed `coin_rng`, as the other generators in this cell already are. Deferred to the author.
- **Final status:** *pending*.

#### E11-03 — Broken Colab link and non-standard badge
- **Location:** cell 0 (no `id`) links to `encontro_11/enc_11_a.ipynb`, which does not exist. The alt text is English, there is no runtime note, and the badge precedes the YAML cell.
- **Severity / class / status:** medium · publication · verified defect.
- **Proposed correction:** point the link to `encontro_11/enc_11.ipynb`. Bringing the badge to the course convention is part of the publication work (deferred).
- **Final status:** *pending*.

#### E11-04 — Duplicated and out-of-order passages
- **Location:**
  - cell 19 (`1qHuCz-Y5hPu`) repeats the H₀/H₁ bullets and formulas of cell 20 (`16bb6397`) verbatim, and wraps `$H_1$` in backticks, so the math renders as literal code;
  - cell 31 (`mh_qv52SUx0l`) repeats the last paragraph of cell 30;
  - cell 34 (`hmFHYCjVVDSV`) announces the SciPy call *after* the call in cell 33;
  - cells 44 and 46 both assign `permutation_p_value`;
  - headings “8.1 Definindo α”, “8.2 O valor-p”, “**8.1** Interpretando o resultado” (cell 45) and “8.3 Interpretando o resultado” (cell 47) duplicate one another;
  - “### Cliff's delta” (cell 54) is followed by “### 9.2 … Cliff's delta” (cell 55);
  - heading 6.3 reads “permutacao”;
  - the heading “Um experimento com uma moeda justa” (cell 21) is followed by text about the burden of proof, not about the coin.
- **Severity / class / status:** medium · pedagogical · verified defect.
- **Proposed correction:** consolidate. Which version of each duplicated passage to keep is an editorial choice, so this is deferred to the author.
- **Final status:** *pending*.

#### E11-05 — Unit of randomisation and independence are not discussed
- **Location:** cells 27–33 and 59.
- **Severity / class / status:** medium · methodological · probable issue.
- **Evidence:** the permutation test treats the 4,105 impressions as exchangeable, independent Bernoulli units. The notebook does not say whether Upworthy randomised impressions, page views or visitors. Repeated impressions to the same visitor would make outcomes dependent, and the p-value and interval would then be too optimistic. Cell 59 rightly makes causal comparison conditional on the randomisation having “funcionado como planejado”, but does not name the unit.
- **Proposed correction:** add one sentence naming the assumed unit and the consequence if impressions are not independent. The exact randomisation unit should come from the archive's documentation (Matias et al., 2021), which was not consulted here. Not implemented, to avoid asserting an unverified fact.
- **Final status:** *pending*.

#### E11-06 — The null-distribution histogram has empty bins between bars
- **Location:** cell 39 (`9c5c8f2c`, `fig-upworthy-nula`), `bins="fd"`.
- **Severity / class / status:** medium · graphical · verified defect.
- **Evidence:** with the margins fixed, T* = k(1/2091 + 1/2014) − 50/2014. The lattice step is 0.0975 p.p., while the FD bin width is about 0.045 p.p. The saved figure shows an empty bin between every pair of bars.
- **Proposed correction:** one bin per possible k, as in E10-01. Optionally shade both tails |T*| ≥ |T_obs| so the two-sided p-value is visible. Deferred, together with the other changes needed for publication.
- **Final status:** *pending*.

#### E11-07 — Missing visual comparisons
- **Severity / class / status:** low · graphical · optional improvement.
- **Evidence:** the only figure is the null distribution. The two CTRs with their uncertainty, and the bootstrap distribution behind the interval [−0.04, 1.31] p.p., are reported only as numbers. Both figures can be built from data already in the notebook (`creature_outcomes`, `monkey_outcomes`, `effect_bootstrap_result.bootstrap_distribution`); nothing would have to be invented.
- **Final status:** *pending* (recommended for the publication PR).

#### E11-08 — Data read only from `refs/heads/main`, provenance undocumented
- **Location:** cell 6 (`3593d4e7`); `DATASETS.md` has no entry for the CSV under `encontro_11/data/`.
- **Severity / class / status:** medium · reproducibility/publication · verified defect.
- **Evidence:** the file exists locally but is never read from disk. The URL tracks `main`, not a fixed commit.
- **Proposed correction:** read the local file first, as the other lessons do (deferred, with the publication work). Add a `DATASETS.md` entry that records only verifiable facts and the gaps (implemented).
- **Final status:** *pending*.

### Encontro 12 — `encontro_12/enc_12.ipynb` (not published)

A fresh execution in a separate environment (see §1) **reproduced every
saved number**: corpus sizes, medians, lexical frequencies, coverage and D_P,
the section means of the five features, Δ = −0.892 with p = 0.0391, the five
F statistics (44.33, 79.78, 67.92, 38.48, 85.64) and the Holm-adjusted
p-values (0.00025).

#### E12-01 — Saved output inconsistent with the code (stale Holm table)
- **Location:** cells 62 (`NxEQ-_zd9zuA`) and 64 (`dHaybIcKWOfj`); counts jump 32 → 36 → 37 → 38 → 41.
- **Severity / class / status:** high (publication) · reproducibility · verified defect.
- **Evidence:** the saved tables contain a column `p-valor_holm` that the current code does not create. A fresh run produces only `p_valor_holm`.
- **Proposed correction:** re-execute from a clean kernel in a documented environment. Deferred (see E12-02).
- **Final status:** *pending*.

#### E12-02 — Dependencies outside the documented environment
- **Location:** cells 3 (`!pip install -q pyarrow`), 33 (`!python -m spacy download …`), 34, 62 and 68.
- **Severity / class / status:** blocker (publication) · reproducibility · verified defect.
- **Evidence:** in the course environment, execution fails at `pd.read_parquet` (no pyarrow), `import spacy`, `statsmodels` and `sklearn` (30 cells fail). The `pt_core_news_sm` version is not pinned, and the data are downloaded from Hugging Face on every run.
- **Proposed correction:** the author must decide whether to extend `scripts/requirements.txt` (and with which spaCy model version) or keep encontro 12 Colab-only. Deferred.
- **Final status:** *pending*.

#### E12-03 — Article-level mean versus pooled sentence-level mean
- **Location:** cells 41, 43, 44 and 47–54.
- **Severity / class / status:** medium · interpretative · probable issue (no error in the computation).
- **Evidence:** “comprimento médio das sentenças” is computed per article (tokens ÷ sentences) and then averaged with equal weight per article. This answers “how long are sentences in a *typical article* of the section?”. A pooled mean (all tokens ÷ all sentences in the section) answers “how long is a *typical sentence*?”. Cell 43 already states the distinction, and the permutation test treats articles as the exchangeable units, which is consistent with the article-level estimand. Pooling sentences and permuting them would violate independence within articles. Values computed with the reproduced annotations are given in §5.
- **Proposed correction:** none to the estimand, which matches the question as stated (“características linguísticas de suas matérias”). Optionally, make the wording in cells 43 and 47 say “média, por matéria, do comprimento médio das sentenças”. Left to the author.
- **Final status:** *pending*.

#### E12-04 — PCA presented as clustering
- **Location:** cell 67 (`revision-pca-method`), heading “## 6. Visualização com Clusters (PCA)”.
- **Severity / class / status:** medium · interpretative/pedagogical · verified defect.
- **Evidence:** PCA is a linear projection, not a clustering algorithm; the cell's own text describes it correctly as a projection.
- **Proposed correction:** change the heading to “## 6. Visualização com componentes principais (PCA)”.
- **Final status:** *pending*.

#### E12-05 — Interpretive axis labels not checked against the loadings
- **Location:** cell 68 (`1jl7DvCqgxfy`); cell 69 (`revision-pca-interpretation`) says the labels “precisam ser conferidas”.
- **Severity / class / status:** medium · interpretative · requires investigation. Loadings are given in §5.
- **Evidence:** the figure has no tick values and prints neither `pca.components_` nor `explained_variance_ratio_`, yet labels both axes with directional claims (“← mais verbos | …”).
- **Proposed correction:** print the loadings and the explained variance next to the figure, and align the labels with them. Deferred; it requires re-execution in the NLP environment.
- **Final status:** *pending*.

#### E12-06 — The legend contradicts the marker
- **Location:** cell 68. The legend says “Ponto branco: centro da seção”, but the marker is `color="darkgrey"`. Cell 69 asks readers to read “ponto branco” as the grey marker.
- **Severity / class / status:** low · graphical · verified defect (confirmed on the saved image).
- **Proposed correction:** draw the marker white with a dark edge, or change the legend text, then remove the sentence in cell 69. Deferred (requires re-execution).
- **Final status:** *pending*.

#### E12-07 — Not ready for the website
- **Evidence:** no YAML/`pagetitle` cell, English badge text, no runtime note, and no `CHECKS` entry in `check_course.py`.
- **Final status:** *pending* (publication blocker, see §6).

The final project (`encontro_12/final_project/enc_12_final_project.ipynb`) is
an unexecuted exercise template. It needs NLTK, spaCy and `en_core_web_sm`.
It was skimmed only; no defects were recorded.

### Homework and answer keys

All four answer keys execute; their outputs match apart from Python's
`help()` formatting.

#### HW-01 — The question names a plot the exercise never asks for
- **Location:** `encontro_9/homework/enc_9_homework.ipynb`, cell 15 (`0a980391`): “Com base nas ECDFs e KDEs”. The tasks ask for an ECDF (cell 11) and histograms (cell 13). Cell 2 (`999168b1`) also has the typo “carregar o as amostras”.
- **Severity / class / status:** low · pedagogical · verified defect.
- **Proposed correction:** “Com base nas ECDFs e nos histogramas”; “carregar as amostras”.
- **Final status:** *pending*.

#### HW-02 — The conclusion cites an analysis the homework does not contain
- **Location:** `encontro_8/homework/enc_8_homework.ipynb`, cell 11 (`8bfcfbaf`) asks students to consider “o resultado da análise de sensibilidade”, but no exercise performs one.
- **Severity / class / status:** low · pedagogical · requires authorial decision (add the exercise or remove the bullet).
- **Final status:** *pending*.

## 4. Repository-wide findings

#### R-01 — CI publishes without running the course validation
- **Location:** `.github/workflows/publish.yml`.
- **Severity / class / status:** medium · reproducibility · verified.
- **Evidence:** the workflow runs only `quarto render`. With `execute.enabled: false`, the site depends entirely on the saved outputs, but `check_course.py` (saved state and site) never runs in CI.
- **Proposed correction:** add a job that runs `scripts/check_course.py --site` after the render (it needs PyYAML, nbformat, nbclient and beautifulsoup4). Not implemented: it changes deployment behaviour and should be the author's decision. Recommended as a separate PR.
- **Final status:** *pending*.

#### R-02 — Validator assertion refers to a variable removed from encontro 8
- **Location:** `scripts/check_course.py`, `CHECKS["encontro_8/enc_8.ipynb"]`, `assert len(gapminder_2007) == 142`.
- **Severity / class / status:** high · computational · verified defect.
- **Evidence:** `gapminder_2007` is defined only in `enc_8-parte2.ipynb` (and asserted there too). In `enc_8.ipynb`, `--execute` would raise `NameError`.
- **Proposed correction:** replace the assertion with checks of what encontro 8 actually computes: 1,704 rows and the symmetric Gapminder Spearman matrix with unit diagonal.
- **Final status:** *pending*.

#### R-03 — The validator cannot catch the class of defect that broke the build
- **Evidence:** E7-01 and E7-02/E8-01 were introduced by an edit made in Colab and passed through unnoticed.
- **Proposed correction:** two source-level checks in `check_notebook()`: (a) `#|` options preceded by blank lines; (b) duplicate `#| label` values within a notebook. Both are small and deterministic.
- **Final status:** *pending*.

#### R-04 — Optional pyarrow changes saved outputs
- **Severity / class / status:** low · reproducibility · verified.
- **Evidence:** pandas `memory usage` in saved `info()` outputs (439.1 KB in enc_10-parte2; 15.2 MB in enc_11) differs from the documented environment (363.0 KB; 2.6 MB). The saved outputs were produced with pyarrow installed, which `requirements.txt` does not pin.
- **Proposed correction:** none (cosmetic). Note it for the author.
- **Final status:** *pending*.

#### R-05 — `DATASETS.md` does not cover encontros 11–12
- **Severity / class / status:** medium · publication · verified.
- **Evidence:** no entry for the Upworthy CSV in the repository, nor for the remote Folha de S.Paulo dataset.
- **Proposed correction:** add short entries with verifiable facts (file, size, columns, cited source) and explicit gaps (acquisition URL, date, licence).
- **Final status:** *pending*.

Website configuration, homepage, sidebar and README: verified and retained.
They consistently list encontros 1–10 (part 2). Branding, attribution, licence
and acknowledgements were not touched.

## 5. Encontro 12: supplementary computations

Computed by appending cells to a scratch copy of the notebook, after a full
fresh run in the environment described in §1. These numbers are evidence for
E12-03 and E12-05; they were not added to the lesson.

**PCA (standardised features).** Explained variance: PC1 46.4%, PC2 24.0%
(70.4% in the plane).

| Feature | PC1 | PC2 |
|---|---:|---:|
| `comprimento_medio_sentenca` | −0.060 | **0.521** |
| `proporcao_nomes_proprios` | **0.611** | −0.029 |
| `proporcao_adjetivos` | −0.178 | **0.714** |
| `proporcao_verbos` | **−0.466** | **−0.463** |
| `densidade_entidades` | **0.612** | −0.064 |

The hard-coded labels in cell 68 are **consistent** with these loadings:
x = “← mais verbos | mais nomes próprios e entidades →”, y = “← mais verbos |
mais adjetivos e sentenças longas →”. The sign of a principal component is
arbitrary, however, and the labels are not derived from the fitted object. A
change of data, sample or library version could reverse an axis without any
visible error. Hence E12-05: print the loadings and derive or check the labels.

**Sentence length: two estimands.**

| Section | Mean of article ratios (notebook) | Pooled: Σ tokens / Σ sentences | Mean sentences per article |
|---|---:|---:|---:|
| colunas | 19.881 | 18.241 | 31.1 |
| esporte | 20.347 | 18.740 | 24.5 |
| ilustrada | 19.641 | 17.618 | 27.6 |
| ilustrissima | 20.774 | 20.242 | 66.7 |
| mercado | **23.860** | 22.224 | 22.6 |
| mundo | 22.866 | 20.863 | 27.5 |
| poder | 23.298 | **22.340** | 24.4 |

- colunas − ilustrissima: −0.892 (article level, as in the notebook) versus **−2.0** (pooled).
- The section with the highest value changes: mercado at article level, poder pooled.

The article-level quantity answers the notebook's stated question and matches
the exchangeable unit of the permutation test. The pooled quantity gives more
weight to long articles. The difference shows why statements about
“sentenças de uma seção” must name the estimand; this is the reason for the
optional wording change in E12-03.

**Verbs, same contrast.** In ilustrissima the article-level mean is 0.0916 and
the pooled value 0.1002. The ordering of sections is not identical under the
two definitions.

**Holm.** `multipletests(…, method="holm")` applied to the five permutation
p-values (each 1/20,000) gives 0.00025 for all five, as in the notebook. The
equality is an artefact of every raw p-value sitting at the Monte Carlo
resolution floor, which cell 59 explains correctly.

## 6. Publication blockers for encontros 11 and 12

Adding the two notebooks to `_quarto.yml` is **not** sufficient and was not done.

| Blocker | Encontro 11 | Encontro 12 |
|---|---|---|
| Executed in order in a documented environment | No (E11-01) | No (E12-01, E12-02) |
| Reproducible saved outputs | No (E11-02) | Yes, numerically; table stale |
| Dependencies in `scripts/requirements.txt` | Yes | No (pyarrow, spaCy + model, scikit-learn, statsmodels) |
| Offline data access | No (E11-08) | No (remote Parquet) |
| Front matter, badge, runtime note | No (E11-03) | No (E12-07) |
| Editorial consolidation | E11-04 | E12-04 to E12-06 |
| Validator `CHECKS` entry | Missing | Missing |
| `DATASETS.md` | R-05 | R-05 |
| Sidebar, homepage, README entries | Missing | Missing |
