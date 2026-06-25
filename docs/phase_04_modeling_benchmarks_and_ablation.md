# Phase 04 — Modeling Fixes, Benchmarks & Ablation

## Objective

Sửa overfitting GraphSAGE, bổ sung baseline mạnh, multi-seed/fold metrics và ablation để chứng minh model học tín hiệu thật.

## Why this phase matters

Paper cần chứng minh GNN có giá trị so với baseline và kết quả không phải artifact của split/seed/dataset nhỏ.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 10 | Fix GraphSAGE overfitting | GraphSAGE training script mới + metrics nhiều seed/fold | Modeling lead | 2-3 days | High priority |
| 11 | Bổ sung model benchmark | Benchmark table chính + supplementary full metrics | Modeling lead | 3-5 days | Research upgrade |
| 12 | Thử nghiệm trên nhiều dataset | Multi-dataset experiment table + dataset summary table | Experiment lead | 5-10 days | Major upgrade |
| 13 | Ablation study | Ablation table + short discussion | Modeling lead | 2-3 days | Research upgrade |


## Phase-level criteria

- Training có early stopping thật với patience, validation metric rõ và checkpoint hợp lệ.
- Report đủ train/val/test metrics, multi-seed hoặc fold, mean ± std/CI.
- Baseline gồm traditional ML và network heuristics, không chỉ random/betweenness nếu không đủ mạnh.
- Ablation trả lời GraphSAGE học gì: no-graph MLP, remove metadata, remove centrality, remove edge/contact features.
- Nếu thêm dataset, có dataset summary, preprocessing tương thích và comparison table.


## Detailed subtasks

### Checklist 10: Fix GraphSAGE overfitting

**Output bàn giao:** GraphSAGE training script mới + metrics nhiều seed/fold  
**Owner đề xuất:** Modeling lead  
**Time estimate:** 2-3 days  
**Ghi chú:** Hiện train AUC 0.9914 vs test AUC 0.7669; report cũng ghi hyperparameter chưa khớp code.  
**Priority note:** High priority

**Subtasks & criteria**
- **10.1 — Implement early stopping thật với patience, không chỉ lưu best epoch rồi chạy đủ 500 epochs**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **10.2 — Tune hidden_dim, dropout, weight_decay, learning rate bằng validation trong CV**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **10.3 — So sánh train/val/test gap qua nhiều seed**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **10.4 — Calibrate probability scores và ưu tiên ranking metrics thay vì threshold-only classification**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **10.5 — Cân nhắc GraphSAGE nhỏ hơn hoặc logistic/ridge baseline nếu dataset vẫn nhỏ**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 11: Bổ sung model benchmark

**Output bàn giao:** Benchmark table chính + supplementary full metrics  
**Owner đề xuất:** Modeling lead  
**Time estimate:** 3-5 days  
**Ghi chú:** Cần chứng minh GNN hơn baseline mạnh, không chỉ hơn random/betweenness.  
**Priority note:** Research upgrade

**Subtasks & criteria**
- **11.1 — Traditional ML: Logistic Regression, Random Forest/XGBoost, SVM nếu phù hợp**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **11.2 — Network baselines: degree, weighted degree, betweenness, closeness, PageRank, k-core, eigenvector**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **11.3 — GNN baselines: GCN, GAT, GraphSAGE variants, MLP-no-graph ablation**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **11.4 — Intervention baselines: random, greedy influence maximization/NetShield/vaccination heuristic nếu triển khai được**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 12: Thử nghiệm trên nhiều dataset

**Output bàn giao:** Multi-dataset experiment table + dataset summary table  
**Owner đề xuất:** Experiment lead  
**Time estimate:** 5-10 days  
**Ghi chú:** Một dataset 340 node là chưa đủ mạnh cho bài nghiên cứu hoàn chỉnh.  
**Priority note:** Major upgrade

**Subtasks & criteria**
- **12.1 — Thêm ít nhất 2 dataset contact network khác: ví dụ SocioPatterns school/workplace/hospital hoặc dataset public phù hợp**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **12.2 — Nếu không có nhãn infection thật, dùng synthetic infection trên empirical networks và tách rõ phần mô phỏng**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **12.3 — Chạy cùng protocol trên từng dataset**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **12.4 — Báo cáo cross-dataset generalization hoặc limitation nếu chỉ có SASHTS**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 13: Ablation study

**Output bàn giao:** Ablation table + short discussion  
**Owner đề xuất:** Modeling lead  
**Time estimate:** 2-3 days  
**Ghi chú:** Ablation giúp trả lời GNN học gì thật sự.  
**Priority note:** Research upgrade

**Subtasks & criteria**
- **13.1 — No-graph MLP vs GraphSAGE**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **13.2 — Remove metadata features**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **13.3 — Remove centrality features**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **13.4 — Unweighted vs weighted adjacency**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **13.5 — Static vs temporal graph nếu có timestamp**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **13.6 — With/without index-case-related features**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
