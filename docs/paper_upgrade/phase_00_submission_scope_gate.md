# Phase 00 - Submission Scope and Compliance Gate

Date: 2026-06-24  
Lead role: Person 1 - Writing and Submission Lead  
Scope: journal/scope gate, article type, reference-style gate, title identity, and title-page evidence only. No modeling, metrics, tables, figures, abstract rewrite, related work rewrite, or cover letter drafting is performed in this phase.

## 1. Repository and Evidence Inventory

Phase 00 began with a repository inspection and a complete read-through of every Markdown file under `docs/`.

Relevant Phase 00 files and artifacts:

| Evidence path | Role in Phase 00 | Status |
|---|---|---|
| `docs/README_PHASE_ROADMAP.md` | Defines the one-phase-at-a-time workflow and global definition of done. | Read |
| `docs/phase_00_submission_scope_gate.md` | Primary Phase 00 checklist and acceptance criteria. | Read |
| `docs/CRITERIA_MATRIX.md` | Micro-criteria for Phase 00 checklist IDs 1, 2, and 3. | Read |
| `docs/CODEX_PROMPT_PACK.md` | Phase execution rules and response requirements. | Read |
| `Template Title Page_JTD.docx` | Local JTD title page template and temporary formatting authority if no other template is confirmed. | Inspected |
| `[SNA] REPORT.docx` | Vietnamese course-style report; source for current authorship evidence and current title style. | Inspected |
| `[SNA] REPORT_EN.docx` | English course-style report; confirms the current document is still a final-project report. | Inspected |
| `reports/report.tex` | LaTeX report source; confirms current title block and course-report framing. | Inspected |
| `README.md` | Current public-facing project summary and research framing. | Inspected |
| `data/raw/SOURCE.md` | Dataset source note and licensing/status summary. | Inspected |
| `results/`, `visualizations/`, `notebooks/`, `scripts/`, `src/` | Relevant downstream artifacts for later phases; no edits in Phase 00. | Inventoried |

## 2. Journal and Scope Gate

### 2.1 Candidate target journal

Working target: **Journal of Thoracic Disease (JTD, AME Publishing Company)**.

Evidence:

- Official author guidelines inspected: `https://jtd.amegroups.org/pages/view/guidelines-for-authors`.
- The official page identifies JTD as an international, peer-reviewed, open-access journal covering respiratory, lung, heart, esophageal, and mediastinal diseases.
- The local repository contains `Template Title Page_JTD.docx`, and the phase documents repeatedly refer to `JTD/AME`, which makes Journal of Thoracic Disease the most plausible interpretation of "JTD" available from the repository plus official web evidence.

Decision status: **Provisional, not final**. The repository does not contain an explicit corresponding-author note confirming that Journal of Thoracic Disease is the intended destination. This must be confirmed before Phase 01 and before any citation-style conversion.

### 2.2 Article type

Provisional article type: **Original Article**.

Rationale:

- COSTTRACE reports an original empirical analysis pipeline using SASHTS contact-network data, graph-based risk modeling, and intervention evaluation artifacts.
- JTD's official author instructions list Original Article as the category for original research investigations and specify a structured abstract and IMRaD-style main text.

Decision status: **Provisional**. Scope fit is not fully locked because COSTTRACE is a computational public-health/network-intervention manuscript rather than a conventional thoracic clinical study. The corresponding author should confirm with the target journal or choose a more computational/public-health-oriented venue if needed.

### 2.3 Scope fit note

COSTTRACE has a plausible but non-trivial fit with JTD if framed as SARS-CoV-2 household transmission analysis and decision support for epidemic intervention. The strongest fit argument is that the dataset concerns SARS-CoV-2 household transmission and the manuscript evaluates methods for prioritizing intervention in epidemic contact networks.

Residual scope risk:

- The work is currently a proof-of-concept computational/network analysis on one household contact dataset.
- The current manuscript does not yet demonstrate clinical deployment, thoracic-disease-specific intervention, or multi-dataset external validity.
- Phase 04 and Phase 05 upgrades may be required before the submission claim is strong enough for a clinical journal.

Gate decision: **Proceed only as a provisional JTD/AME track until the corresponding author confirms the exact journal and article type.**

### 2.4 Reference style gate

Provisional style if Journal of Thoracic Disease is confirmed: **Vancouver style**.

Evidence:

- The official JTD author instruction page includes a manuscript style section for Vancouver Style.
- `docs/phase_08_language_references_submission_package.md` explicitly notes that JTD/AME uses Vancouver, while the local checklist/template may currently point toward APA 7.

Gate decision: **Do not convert references in Phase 00.** Citation conversion belongs to Phase 08 after the target journal is final.

## 3. Title Identity Gate

The current course-report title evidence includes:

- `reports/report.tex`: `Budget-Constrained Epidemic Intervention on Contact Networks`.
- `[SNA] REPORT.docx` and `[SNA] REPORT_EN.docx`: `Budget-Constrained Adaptive Intervention in Temporal Epidemic Contact Networks`.

The second title overclaims the current evidence because the implemented graph is effectively static at the analysis level and the report does not establish adaptive/temporal intervention claims across multiple datasets. Phase 00 therefore removes "adaptive", avoids "optimal", and narrows the setting to household epidemic contact networks.

### Recommended working title

English title:

**Budget-Constrained Node Intervention in Household Epidemic Contact Networks Using Graph Learning**

Vietnamese title:

**CAN THIỆP NODE CÓ RÀNG BUỘC NGÂN SÁCH TRÊN MẠNG TIẾP XÚC DỊCH TỄ HỘ GIA ĐÌNH BẰNG HỌC ĐỒ THỊ**

Running title candidate:

**Budgeted Intervention in Household Contact Networks**

### Alternative title options for PI/corresponding-author selection

1. **Graph Learning for Budget-Constrained Intervention in Household Epidemic Contact Networks**
2. **Budget-Constrained Epidemic Intervention in Household Contact Networks with Graph Learning**
3. **Prioritizing Nodes for Budget-Constrained Intervention in Household Epidemic Contact Networks**

Title gate status: **Working title selected, final human confirmation required.**

## 4. Title Page Gate

The local template `Template Title Page_JTD.docx` contains these required fields:

- Vietnamese title in uppercase.
- English title in uppercase.
- Author names.
- Author affiliations.
- Author emails.
- Vietnamese abstract.
- Vietnamese keywords.
- English abstract.
- English keywords.
- Corresponding author.
- Corresponding-author phone.
- ORCID if available.
- Consistency note requiring title-page information to match the final manuscript.

Evidence currently available:

| Field | Evidence available now | Phase 00 status |
|---|---|---|
| Vietnamese title | Working title proposed in this gate file. | Ready for confirmation |
| English title | Working title proposed in this gate file. | Ready for confirmation |
| Author names | `[SNA] REPORT.docx` lists Nguyễn Quốc Khánh, Ngô Chánh Phong, Dương Quang Đông, Nguyễn Đình Lương. | Partial |
| Author affiliations | Template placeholder only. No publication affiliation evidence found. | Missing |
| Author emails | Template placeholder only. No email evidence found. | Missing |
| Corresponding author | Not specified in repository evidence. | Missing |
| Phone | Template placeholder only. | Missing |
| ORCID | Template placeholder only. | Missing |
| Abstract and keywords | Phase 01 deliverable, not Phase 00. | Deferred |
| Word count, figures/tables count, author contributions | Required by JTD official title page guidance, but not available until manuscript structure is finalized. | Deferred |

Gate decision: **Do not generate a submission-ready title page DOCX yet.** Producing a "complete" title page would require inventing author affiliations, emails, corresponding-author details, ORCID, abstract, and keywords. Instead, this file records the exact missing inputs as TODOs.

## 5. Phase 00 TODOs

| TODO ID | Owner | Missing input | Why it blocks Phase 00 completion |
|---|---|---|---|
| TODO-P00-01 | Corresponding author | Confirm exact target journal: Journal of Thoracic Disease or another JTD/local venue. Include official guideline URL or local instruction file. | Required before citation style, article type, and formatting decisions are final. |
| TODO-P00-02 | Corresponding author | Confirm article type: Original Article, Research Article, Brief Report, or other. | Required before abstract structure, word limits, title page, and reporting checklist are final. |
| TODO-P00-03 | Corresponding author / Writing lead | Confirm whether the local `Template Title Page_JTD.docx` overrides or supplements the official AME/JTD title-page requirements. | Required before generating the final title page file. |
| TODO-P00-04 | All authors / Writing lead | Provide final author order, full author names, affiliations, institutional addresses, and email addresses. | Required for title page. |
| TODO-P00-05 | Corresponding author | Select corresponding author and provide phone number, full address, email, and ORCID if available. | Required for title page and submission metadata. |
| TODO-P00-06 | PI / Writing lead | Confirm final bilingual title from the recommended title and alternatives above. | Required before rewriting manuscript identity in Phase 01. |
| TODO-P00-07 | Data owner / Corresponding author | Confirm whether raw SASHTS files may be included in any public submission/release package or only referenced as restricted academic data. | Required to preserve confidentiality and licensing constraints. |
| TODO-P00-08 | Writing lead | Provide or approve Vietnamese and English abstract/keywords after Phase 01 drafting. | Required before title page can be completed. |

## 6. Phase 00 Acceptance Status

| Checklist ID | Required deliverable | Phase 00 status | Evidence / blocker |
|---:|---|---|---|
| 1 | Official guideline link + article type + scope fit note | Partially addressed | Official JTD guideline identified; article type and scope are provisional pending corresponding-author confirmation. |
| 2 | Completed title page using local JTD template | Blocked | Template inspected, but author metadata and abstracts are missing. See TODO-P00-04, TODO-P00-05, TODO-P00-08. |
| 3 | Final Vietnamese and English title | Partially addressed | Working title and alternatives provided; final selection requires PI/corresponding-author confirmation. |

## 7. Commands and Checks Run

Key local commands:

```powershell
Get-ChildItem -Force
rg --files
git status --short --branch
Get-ChildItem docs -File -Filter *.md
Get-Content -Raw docs\README_PHASE_ROADMAP.md
Get-Content -Raw docs\phase_00_submission_scope_gate.md
Get-Content -Raw docs\phase_01_manuscript_identity_and_framing.md
Get-Content -Raw docs\phase_02_related_work_and_research_positioning.md
Get-Content -Raw docs\phase_03_dataset_protocol_and_leakage_control.md
Get-Content -Raw docs\phase_04_modeling_benchmarks_and_ablation.md
Get-Content -Raw docs\phase_05_simulation_counterfactual_and_budget_evaluation.md
Get-Content -Raw docs\phase_06_results_figures_tables_and_narrative.md
Get-Content -Raw docs\phase_07_reproducibility_testing_and_supplement.md
Get-Content -Raw docs\phase_08_language_references_submission_package.md
Get-Content -Raw docs\CODEX_PROMPT_PACK.md
Get-Content docs\CRITERIA_MATRIX.md | Select-Object -First 260
Get-Content docs\CRITERIA_MATRIX.md | Select-Object -Skip 260 -First 260
Get-Content docs\CRITERIA_MATRIX.md | Select-Object -Skip 520 -First 260
```

Document inspection:

```powershell
# Bundled Python was used to extract paragraph text from DOCX files without editing them.
C:\Users\Acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -c "<zipfile/xml paragraph extraction>" "Template Title Page_JTD.docx" "[SNA] REPORT.docx" "[SNA] REPORT_EN.docx"
```

Web evidence inspected:

- Official JTD author guidelines: `https://jtd.amegroups.org/pages/view/guidelines-for-authors`

Validation checks:

- All Markdown files under `docs/` were read.
- `Template Title Page_JTD.docx` was inspected structurally before any title page decision.
- No manuscript, notebook, source code, dataset, result, figure, or model artifact was modified in Phase 00.
- Missing evidence was converted into explicit TODOs rather than filled with invented metadata.

## 8. Remaining Risks

- JTD may not be the final intended journal despite strong local signals from `Template Title Page_JTD.docx` and the docs references to JTD/AME.
- Even if JTD is confirmed, scope fit remains uncertain because the paper is currently a computational proof-of-concept rather than a thoracic clinical trial or observational clinical study.
- Title page generation is blocked until author metadata and corresponding-author details are provided.
- Phase 01 should not rewrite the abstract or manuscript structure until TODO-P00-01, TODO-P00-02, and TODO-P00-06 are resolved or explicitly accepted as provisional by the team.
