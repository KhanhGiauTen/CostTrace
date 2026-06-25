# COSTTRACE Research Paper Upgrade — Phase Roadmap

Generated from `CHECKLIST.xlsx` / sheet `JTD Checklist`.

## Purpose

This folder converts the 32 checklist items into staged Markdown phases for revising the project into a research paper.  
Use one phase at a time with Codex to avoid mixing journal compliance, writing, modeling, simulation, reproducibility, and submission tasks.

## Recommended order

| Phase | Focus | Checklist IDs | Priority |
|---|---|---:|---|
| [Phase 00 — Submission Scope & Compliance Gate](./phase_00_submission_scope_gate.md) | Khóa đích nộp, article type, template, citation style, title page và title trước khi sửa nội dung sâu. | 1, 2, 3 | Critical gate |
| [Phase 01 — Manuscript Identity, Abstract, RQ & Paper Conversion](./phase_01_manuscript_identity_and_framing.md) | Chuyển bản report/course project thành manuscript nghiên cứu có abstract, novelty, research questions và cấu trúc paper rõ ràng. | 4, 5, 6 | High |
| [Phase 02 — Related Work, Novelty Positioning & Citation Base](./phase_02_related_work_and_research_positioning.md) | Nâng literature review từ mức báo cáo môn học lên mức bài nghiên cứu có khung học thuật và citation base sạch. | 7 | High |
| [Phase 03 — Dataset, Preprocessing, Split Protocol & Leakage Audit](./phase_03_dataset_protocol_and_leakage_control.md) | Làm rõ dữ liệu SASHTS, preprocessing, graph construction và loại bỏ nguy cơ leakage trong evaluation. | 8, 9, 23, 24 | Reviewer-critical |
| [Phase 04 — Modeling Fixes, Benchmarks & Ablation](./phase_04_modeling_benchmarks_and_ablation.md) | Sửa overfitting GraphSAGE, bổ sung baseline mạnh, multi-seed/fold metrics và ablation để chứng minh model học tín hiệu thật. | 10, 11, 12, 13 | Major research upgrade |
| [Phase 05 — SIR Sensitivity, Counterfactual Evaluation & Budget Curves](./phase_05_simulation_counterfactual_and_budget_evaluation.md) | Chuẩn hóa mô phỏng epidemic intervention, counterfactual assumption, budget/cost setting và uncertainty. | 14, 15, 16, 17 | Reviewer-critical |
| [Phase 06 — Results Narrative, Figures, Tables & Consistency Audit](./phase_06_results_figures_tables_and_narrative.md) | Đóng gói kết quả thành narrative nghiên cứu: bảng/figure chuẩn, đồng bộ số liệu code-report và limitations thuyết phục. | 18, 19, 20, 27, 28 | Visible polish + interpretation |
| [Phase 07 — Reproducibility, Testing & Supplementary Package](./phase_07_reproducibility_testing_and_supplement.md) | Tạo package tái lập kết quả: environment pinning, test suite, run commands, supplementary appendix và release structure. | 21, 22, 29 | Submission strength |
| [Phase 08 — Language, References, Cover Letter & Final Submission Gate](./phase_08_language_references_submission_package.md) | Hoàn thiện bản nộp cuối: language polishing, citation style, cover letter, final format và internal reviewer sign-off. | 25, 26, 30, 31, 32 | Final gate |


## Global Definition of Done

A phase is complete only when:

1. Required files/artifacts are created or updated.
2. The output is traceable to checklist item IDs.
3. Any claim, metric, figure, or table is backed by code, data artifact, or explicit source.
4. Validation commands are recorded.
5. Remaining blockers are written as TODOs, not hidden assumptions.
6. No unrelated refactor or formatting churn is introduced.

## Suggested repository location

Create a working folder in the repo:

```text
docs/paper_upgrade/
├── phase_00_submission_scope_gate.md
├── phase_01_manuscript_identity_and_framing.md
├── ...
└── phase_08_language_references_submission_package.md
```

