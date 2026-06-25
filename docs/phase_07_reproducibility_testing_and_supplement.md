# Phase 07 — Reproducibility, Testing & Supplementary Package

## Objective

Tạo package tái lập kết quả: environment pinning, test suite, run commands, supplementary appendix và release structure.

## Why this phase matters

Reproducibility giúp paper đáng tin hơn và giảm rủi ro reviewer/editor bắt lỗi kỹ thuật.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 21 | Reproducibility package | Reproduction instructions + pinned environment | Engineering lead | 2 days | Supplement |
| 22 | Testing và code quality | tests/ + CI/local test command | Engineering lead | 2-3 days | Robustness |
| 29 | Supplementary material | Supplementary Appendix + GitHub/release package | Reproducibility lead | 1-2 days | Submission package |


## Phase-level criteria

- requirements.txt/environment.yml/pyproject pin version đủ để tái chạy pipeline.
- Có README reproduction commands từ raw/interim data đến tables/figures.
- Có tests cho curation, graph construction, metrics, SIR probability và artifact consistency.
- Supplementary appendix chứa pipeline, feature encoding, hyperparameters, full result tables và extra figures.
- Không đưa dữ liệu nhạy cảm/không có license vào repo public.


## Detailed subtasks

### Checklist 21: Reproducibility package

**Output bàn giao:** Reproduction instructions + pinned environment  
**Owner đề xuất:** Engineering lead  
**Time estimate:** 2 days  
**Ghi chú:** Hiện requirements chưa pin version; pipeline chạy được nhưng chưa đủ chuẩn reproducibility.  
**Priority note:** Supplement

**Subtasks & criteria**
- **21.1 — Pin version trong requirements.txt hoặc tạo environment.yml/pyproject**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **21.2 — Thêm config YAML cho seed, beta/gamma, budget levels, dataset paths**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **21.3 — Tạo Makefile hoặc run_all.ps1 để tái tạo toàn bộ kết quả**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **21.4 — Thêm README paper reproduction: data download, run, expected outputs**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **21.5 — Lưu commit hash/code version trong manuscript**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 22: Testing và code quality

**Output bàn giao:** tests/ + CI/local test command  
**Owner đề xuất:** Engineering lead  
**Time estimate:** 2-3 days  
**Ghi chú:** main.py có phase notebooks; report lại nhắc reporting. Cần thống nhất.  
**Priority note:** Robustness

**Subtasks & criteria**
- **22.1 — Thêm unit tests cho curation, graph construction, metrics, SIR probability, top-k selection**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **22.2 — Thêm smoke test chạy pipeline trên sample nhỏ**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **22.3 — Tránh hard-coded row counts nếu dataset version thay đổi; chuyển sang validation có thông báo rõ**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **22.4 — Chuẩn hóa logging và CLI phase names trong README/report/main.py**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 29: Supplementary material

**Output bàn giao:** Supplementary Appendix + GitHub/release package  
**Owner đề xuất:** Reproducibility lead  
**Time estimate:** 1-2 days  
**Ghi chú:** Appendix hiện có nhưng vẫn dạng đồ án; cần chuyển sang technical supplement.  
**Priority note:** Submission package

**Subtasks & criteria**
- **29.1 — Đưa full pipeline, feature encoding, hyperparameters, full result tables, extra figures, data dictionary mapping**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **29.2 — Thêm model cards/config, random seeds, runtime, hardware**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **29.3 — Đưa notebooks đã cleaned hoặc link GitHub release**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **29.4 — Nếu dữ liệu không phân phối lại được, chỉ cung cấp script xử lý và hướng dẫn tải dữ liệu**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
