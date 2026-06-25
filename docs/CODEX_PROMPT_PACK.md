# Codex Prompt Pack — COSTTRACE Paper Upgrade

## Phase 00 — Submission Scope & Compliance Gate

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 00 — Submission Scope & Compliance Gate
Checklist IDs: 1, 2, 3

Goal:
Khóa đích nộp, article type, template, citation style, title page và title trước khi sửa nội dung sâu.

Scope:
Docs/template audit; không sửa mô hình hoặc số liệu.

Checklist deliverables:
- [1] Xác nhận đích nộp: Link guideline chính thức + quyết định article type + scope fit note
- [2] Title page theo mẫu JTD local: File title page hoàn chỉnh theo Template Title Page_JTD.docx
- [3] Đổi tiêu đề nghiên cứu: Vietnamese title + English title đã chốt

Quality criteria:
- Có bằng chứng guideline/template chính thức hoặc file local được chỉ định làm chuẩn tạm thời.
- Chốt rõ article type: Original Article/Research Article/khác.
- Title không còn màu sắc đồ án/course project; phản ánh đúng research problem, method và setting.
- Title page đủ metadata theo template đang dùng.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 01 — Manuscript Identity, Abstract, RQ & Paper Conversion

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 01 — Manuscript Identity, Abstract, RQ & Paper Conversion
Checklist IDs: 4, 5, 6

Goal:
Chuyển bản report/course project thành manuscript nghiên cứu có abstract, novelty, research questions và cấu trúc paper rõ ràng.

Scope:
Manuscript restructuring and academic writing; không invent kết quả mới.

Checklist deliverables:
- [4] Viết lại Abstract/Tóm tắt: Tóm tắt song ngữ + 4-6 keywords
- [5] Tái cấu trúc manuscript: Manuscript .docx nghiên cứu, không còn dạng báo cáo cuối kỳ
- [6] Làm rõ novelty và research questions: Contribution paragraph + RQ cuối Introduction

Quality criteria:
- Main manuscript không còn Preface, lời cảm ơn môn học, TOC, thông tin lớp học hoặc dấu vết final project report.
- Abstract có Background, Objective, Methodology, Findings, Implications; đúng giới hạn từ và keyword theo đích nộp.
- Introduction kết thúc bằng 2–3 research questions có thể kiểm định và contribution paragraph rõ ràng.
- Claim trong Introduction không vượt quá evidence hiện có.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 02 — Related Work, Novelty Positioning & Citation Base

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 02 — Related Work, Novelty Positioning & Citation Base
Checklist IDs: 7

Goal:
Nâng literature review từ mức báo cáo môn học lên mức bài nghiên cứu có khung học thuật và citation base sạch.

Scope:
Literature structure and citation placeholders; Codex không tự bịa paper nếu chưa có source.

Checklist deliverables:
- [7] Cập nhật literature review: Related Work mới + reference library sạch

Quality criteria:
- Related Work bao phủ các nhóm nghiên cứu chính, không chỉ dựa vào DeepTrace.
- Mỗi nhóm literature có synthesis, gap và connection với COSTTRACE.
- Citation library sạch: không trùng, không sai metadata, không thiếu DOI/venue nếu có.
- Ưu tiên nguồn 2020–2026 nhưng không bỏ qua nền tảng kinh điển nếu cần.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 03 — Dataset, Preprocessing, Split Protocol & Leakage Audit

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 03 — Dataset, Preprocessing, Split Protocol & Leakage Audit
Checklist IDs: 8, 9, 23, 24

Goal:
Làm rõ dữ liệu SASHTS, preprocessing, graph construction và loại bỏ nguy cơ leakage trong evaluation.

Scope:
Dataset docs, split code/protocol, leakage audit; không đổi label semantics nếu chưa có lý do.

Checklist deliverables:
- [8] Chuẩn hóa dữ liệu SASHTS: Dataset section + preprocessing flowchart
- [9] Audit leakage và split protocol: Revised evaluation protocol + leakage audit table
- [23] Ethics, privacy, and data availability: Ethics + Data Availability + AI disclosure text
- [24] Reporting checklist phù hợp: Reporting checklist completed

Quality criteria:
- Dataset section mô tả nguồn, license/access, thời gian thu thập, sensor, biến chính, preprocessing và graph construction.
- Có preprocessing flowchart hoặc textual pipeline có thể tái lập.
- Không dùng node-level random split nếu household/component overlap gây leakage; ưu tiên household-level split hoặc leave-one-household-out.
- Có leakage audit table nêu nguy cơ, mitigation và residual risk.
- Có Ethics, Data Availability, AI disclosure và reporting checklist phù hợp.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 04 — Modeling Fixes, Benchmarks & Ablation

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 04 — Modeling Fixes, Benchmarks & Ablation
Checklist IDs: 10, 11, 12, 13

Goal:
Sửa overfitting GraphSAGE, bổ sung baseline mạnh, multi-seed/fold metrics và ablation để chứng minh model học tín hiệu thật.

Scope:
Model training/evaluation scripts and tables; không cherry-pick seed.

Checklist deliverables:
- [10] Fix GraphSAGE overfitting: GraphSAGE training script mới + metrics nhiều seed/fold
- [11] Bổ sung model benchmark: Benchmark table chính + supplementary full metrics
- [12] Thử nghiệm trên nhiều dataset: Multi-dataset experiment table + dataset summary table
- [13] Ablation study: Ablation table + short discussion

Quality criteria:
- Training có early stopping thật với patience, validation metric rõ và checkpoint hợp lệ.
- Report đủ train/val/test metrics, multi-seed hoặc fold, mean ± std/CI.
- Baseline gồm traditional ML và network heuristics, không chỉ random/betweenness nếu không đủ mạnh.
- Ablation trả lời GraphSAGE học gì: no-graph MLP, remove metadata, remove centrality, remove edge/contact features.
- Nếu thêm dataset, có dataset summary, preprocessing tương thích và comparison table.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 05 — SIR Sensitivity, Counterfactual Evaluation & Budget Curves

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 05 — SIR Sensitivity, Counterfactual Evaluation & Budget Curves
Checklist IDs: 14, 15, 16, 17

Goal:
Chuẩn hóa mô phỏng epidemic intervention, counterfactual assumption, budget/cost setting và uncertainty.

Scope:
Simulation/evaluation scripts and result export; tránh causal wording quá mạnh.

Checklist deliverables:
- [14] Sensitivity analysis cho SIR: Sensitivity plots + SIR parameter table
- [15] Làm rõ counterfactual evaluation: Counterfactual Methods + Results được viết lại
- [16] Mở rộng budget/cost setting: Budget curve + decision table
- [17] Bổ sung thống kê và uncertainty: Statistical analysis subsection + CI in tables/figures

Quality criteria:
- Không chỉ báo cáo một cấu hình beta/gamma/T; có grid hoặc sensitivity analysis.
- Có định nghĩa rõ transmission edge, blocked transmission, intervention timing và giả định counterfactual.
- Budget curve chạy nhiều mức k hoặc cost setting liên tục, không chỉ 1%, 5%, 10%.
- Có bootstrap CI/permutation/randomization test nếu phù hợp.
- Figure và table được generate từ script, không reconstruct thủ công từ aggregate summary.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 06 — Results Narrative, Figures, Tables & Consistency Audit

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 06 — Results Narrative, Figures, Tables & Consistency Audit
Checklist IDs: 18, 19, 20, 27, 28

Goal:
Đóng gói kết quả thành narrative nghiên cứu: bảng/figure chuẩn, đồng bộ số liệu code-report và limitations thuyết phục.

Scope:
Visualization/report generation and manuscript result prose; không thay số liệu bằng tay.

Checklist deliverables:
- [18] Regenerate figures bằng tiếng Anh: Figure folder paper_ready/ + captions tiếng Anh
- [19] Chuẩn hóa bảng: Main tables + supplementary tables
- [20] Đồng bộ số liệu giữa code và report: Consistency audit passed + generated manuscript tables
- [27] Main results narrative: Results + Discussion rewritten around claims
- [28] Limitations and future work: Limitations section thành thật và thuyết phục

Quality criteria:
- Tất cả figure tiếng Anh: title, axis, legend, annotation và caption.
- Main tables thống nhất format, decimal places, metric names và source artifact.
- Manuscript kể 3 thông điệp chính thay vì chỉ liệt kê bảng.
- Có consistency audit giữa code artifact, figure, table và manuscript.
- Limitations thành thật: small graph, household-only components, missing timestamps, single region/context, external validity.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 07 — Reproducibility, Testing & Supplementary Package

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 07 — Reproducibility, Testing & Supplementary Package
Checklist IDs: 21, 22, 29

Goal:
Tạo package tái lập kết quả: environment pinning, test suite, run commands, supplementary appendix và release structure.

Scope:
Engineering/reproducibility package; giữ public/privacy constraints.

Checklist deliverables:
- [21] Reproducibility package: Reproduction instructions + pinned environment
- [22] Testing và code quality: tests/ + CI/local test command
- [29] Supplementary material: Supplementary Appendix + GitHub/release package

Quality criteria:
- requirements.txt/environment.yml/pyproject pin version đủ để tái chạy pipeline.
- Có README reproduction commands từ raw/interim data đến tables/figures.
- Có tests cho curation, graph construction, metrics, SIR probability và artifact consistency.
- Supplementary appendix chứa pipeline, feature encoding, hyperparameters, full result tables và extra figures.
- Không đưa dữ liệu nhạy cảm/không có license vào repo public.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

## Phase 08 — Language, References, Cover Letter & Final Submission Gate

```text
You are Codex working inside the local research repository for the COSTTRACE paper.

PHASE: Phase 08 — Language, References, Cover Letter & Final Submission Gate
Checklist IDs: 25, 26, 30, 31, 32

Goal:
Hoàn thiện bản nộp cuối: language polishing, citation style, cover letter, final format và internal reviewer sign-off.

Scope:
Final manuscript and submission package; không thay đổi kết quả nghiên cứu trừ khi phát hiện lỗi.

Checklist deliverables:
- [25] References và citation style: Reference list final + citation audit
- [26] Language polishing: Polished English manuscript + Vietnamese abstract if required
- [30] Cover letter: Cover letter bản nộp
- [31] Final format pass: Submission-ready package
- [32] Internal pre-submission review: Reviewer-style comments resolved + final sign-off

Quality criteria:
- Reference style đúng journal đã chốt; citation audit không còn missing/unused/duplicate references.
- English academic prose rõ, không còn văn phong report dịch máy.
- Cover letter 1 trang: problem, novelty, dataset, main findings, why readers care, ethics/data statement.
- Final format đúng font, line spacing, margins, page numbering, line numbers và file package yêu cầu.
- Có internal pre-submission review với reviewer-style comments được resolve.

Working rules:
1. First inspect the repository structure and identify the manuscript, notebooks, scripts, data artifacts, figure folders, and existing report files relevant to this phase.
2. Do not invent results, sources, journal rules, citations, datasets, or metrics. If evidence is missing, create an explicit TODO with the exact missing input.
3. Keep changes limited to this phase. Do not refactor unrelated modules.
4. Prefer reproducible scripts over manual edits. Any table/figure in the manuscript should trace back to a code artifact where possible.
5. Preserve confidentiality and do not expose private or non-licensed data in public-facing files.
6. After editing, produce a concise phase report with:
   - files changed,
   - commands run,
   - artifacts generated,
   - validation checks passed/failed,
   - unresolved TODOs and blockers.

Implementation steps:
1. Create or update a phase checklist file under `docs/paper_upgrade/`.
2. Apply the smallest safe changes needed for this phase.
3. Run available tests or lightweight validation scripts.
4. If tests are absent and this phase touches code, add minimal tests or a validation script.
5. Update the manuscript/appendix only when the underlying evidence is available.

Final response format:
- Summary of changes
- Evidence paths
- Validation result
- Remaining risks
```

