# Phase 06 — Results Narrative, Figures, Tables & Consistency Audit

## Objective

Đóng gói kết quả thành narrative nghiên cứu: bảng/figure chuẩn, đồng bộ số liệu code-report và limitations thuyết phục.

## Why this phase matters

Kết quả tốt nhưng trình bày rời rạc sẽ làm reviewer khó thấy contribution; mismatch số liệu dễ gây mất trust.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 18 | Regenerate figures bằng tiếng Anh | Figure folder paper_ready/ + captions tiếng Anh | Visualization lead | 1-2 days | Visible polish |
| 19 | Chuẩn hóa bảng | Main tables + supplementary tables | Writing/Stats lead | 1-2 days | Format |
| 20 | Đồng bộ số liệu giữa code và report | Consistency audit passed + generated manuscript tables | Reproducibility lead | 1 day | Quality control |
| 27 | Main results narrative | Results + Discussion rewritten around claims | Writing/Stats lead | 3h | Interpretation |
| 28 | Limitations and future work | Limitations section thành thật và thuyết phục | Writing lead | 2h | Reviewer trust |


## Phase-level criteria

- Tất cả figure tiếng Anh: title, axis, legend, annotation và caption.
- Main tables thống nhất format, decimal places, metric names và source artifact.
- Manuscript kể 3 thông điệp chính thay vì chỉ liệt kê bảng.
- Có consistency audit giữa code artifact, figure, table và manuscript.
- Limitations thành thật: small graph, household-only components, missing timestamps, single region/context, external validity.


## Detailed subtasks

### Checklist 18: Regenerate figures bằng tiếng Anh

**Output bàn giao:** Figure folder paper_ready/ + captions tiếng Anh  
**Owner đề xuất:** Visualization lead  
**Time estimate:** 1-2 days  
**Ghi chú:** Một số visualization ngoài visualizations/ đã tiếng Anh; notebook figures vẫn còn tiếng Việt.  
**Priority note:** Visible polish

**Subtasks & criteria**
- **18.1 — Sửa toàn bộ title, axis, legend, annotation trong notebooks/reporting sang tiếng Anh**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **18.2 — Ưu tiên vector/SVG hoặc PNG 300-600 dpi**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **18.3 — Dùng style thống nhất, không quá nhiều màu, font đọc được khi in grayscale**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **18.4 — Figure caption trong manuscript phải tự đủ nghĩa và nêu n/sample/metric**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **18.5 — Kiểm tra results/figures/topology/*.png đang còn tiếng Việt**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 19: Chuẩn hóa bảng

**Output bàn giao:** Main tables + supplementary tables  
**Owner đề xuất:** Writing/Stats lead  
**Time estimate:** 1-2 days  
**Ghi chú:** Nếu theo local checklist hiện có thì đang hướng APA 7; nếu JTD/AME thì cần Vancouver/JTD style.  
**Priority note:** Format

**Subtasks & criteria**
- **19.1 — Bảng Dataset, Model Performance, Intervention Results, Ablation, Sensitivity**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **19.2 — Thêm n, metric definition, mean/CI, units**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **19.3 — Caption bảng đặt đúng theo guideline JTD đã xác nhận**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **19.4 — Không nhồi bảng quá lớn vào main text; đưa full table vào supplementary**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 20: Đồng bộ số liệu giữa code và report

**Output bàn giao:** Consistency audit passed + generated manuscript tables  
**Owner đề xuất:** Reproducibility lead  
**Time estimate:** 1 day  
**Ghi chú:** Đây là lỗi nhỏ nhưng reviewer/editor rất dễ bắt.  
**Priority note:** Quality control

**Subtasks & criteria**
- **20.1 — Sửa mismatch tên artifact: report nhắc sir_results.csv nhưng repo có sir_intervention_results.csv**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **20.2 — Sửa mismatch hyperparameters: code dropout 0.35/0.20, report ghi 0.40**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **20.3 — Đảm bảo mọi số trong paper đọc từ results/* mới nhất**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **20.4 — Tạo script generate_tables.py để xuất bảng manuscript từ CSV/JSON**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 27: Main results narrative

**Output bàn giao:** Results + Discussion rewritten around claims  
**Owner đề xuất:** Writing/Stats lead  
**Time estimate:** 3h  
**Ghi chú:** Dựa trên final_comparison.csv và final_strategy_summary.json hiện có.  
**Priority note:** Interpretation

**Subtasks & criteria**
- **27.1 — Viết kết quả thành 3 thông điệp chính, không chỉ liệt kê bảng**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **27.2 — Nhấn mạnh conditional recommendation: degree tốt ở k=1%, GNN tốt ở k=5/10%**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **27.3 — Giải thích vì sao dynamic duration coverage của degree cao nhưng prevention/SIR chưa luôn cao**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **27.4 — Tách observed result khỏi interpretation**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 28: Limitations and future work

**Output bàn giao:** Limitations section thành thật và thuyết phục  
**Owner đề xuất:** Writing lead  
**Time estimate:** 2h  
**Ghi chú:** Report hiện đã có limitations nhưng cần đưa về chuẩn paper và gắn với threats to validity.  
**Priority note:** Reviewer trust

**Subtasks & criteria**
- **28.1 — Nêu rõ small graph, household-only components, missing timestamps for Klerksdorp, single dataset, simplified SIR, potential leakage, no real deployment**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **28.2 — Đề xuất temporal graph, recovery-aware intervention, multi-dataset validation, SEIR, online intervention system**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **28.3 — Không biến future work thành phần thay thế cho experiment bắt buộc nếu claim quá mạnh**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
