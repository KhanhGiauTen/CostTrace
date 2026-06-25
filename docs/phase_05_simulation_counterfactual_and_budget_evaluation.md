# Phase 05 — SIR Sensitivity, Counterfactual Evaluation & Budget Curves

## Objective

Chuẩn hóa mô phỏng epidemic intervention, counterfactual assumption, budget/cost setting và uncertainty.

## Why this phase matters

COSTTRACE mạnh nhất ở decision under budget, nên phần SIR/counterfactual phải có assumption rõ, sensitivity và uncertainty.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 14 | Sensitivity analysis cho SIR | Sensitivity plots + SIR parameter table | Simulation lead | 3-5 days | Reviewer-critical |
| 15 | Làm rõ counterfactual evaluation | Counterfactual Methods + Results được viết lại | Evaluation lead | 2 days | Causal wording |
| 16 | Mở rộng budget/cost setting | Budget curve + decision table | Experiment lead | 2-3 days | Paper value |
| 17 | Bổ sung thống kê và uncertainty | Statistical analysis subsection + CI in tables/figures | Statistics lead | 2 days | Submission strength |


## Phase-level criteria

- Không chỉ báo cáo một cấu hình beta/gamma/T; có grid hoặc sensitivity analysis.
- Có định nghĩa rõ transmission edge, blocked transmission, intervention timing và giả định counterfactual.
- Budget curve chạy nhiều mức k hoặc cost setting liên tục, không chỉ 1%, 5%, 10%.
- Có bootstrap CI/permutation/randomization test nếu phù hợp.
- Figure và table được generate từ script, không reconstruct thủ công từ aggregate summary.


## Detailed subtasks

### Checklist 14: Sensitivity analysis cho SIR

**Output bàn giao:** Sensitivity plots + SIR parameter table  
**Owner đề xuất:** Simulation lead  
**Time estimate:** 3-5 days  
**Ghi chú:** Hiện chart_sir_baseline được reconstruct từ aggregate summary; cần tạo time-series thật cho paper.  
**Priority note:** Reviewer-critical

**Subtasks & criteria**
- **14.1 — Chạy grid beta/gamma/T thay vì chỉ beta=0.25, gamma=0.10, T=30**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **14.2 — Tăng Monte Carlo runs lên 500-1000 nếu runtime cho phép**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **14.3 — Báo cáo mean, 95% CI và robustness ranking theo từng tham số**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **14.4 — Cân nhắc SEIR hoặc recovery-aware intervention**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **14.5 — Không vẽ curve tái dựng nếu không lưu time-series simulation thật**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 15: Làm rõ counterfactual evaluation

**Output bàn giao:** Counterfactual Methods + Results được viết lại  
**Owner đề xuất:** Evaluation lead  
**Time estimate:** 2 days  
**Ghi chú:** Hiện GNN chọn 100% SARS+ và nhiều index cases; cần giải thích thời điểm can thiệp.  
**Priority note:** Causal wording

**Subtasks & criteria**
- **15.1 — Định nghĩa rõ transmission edge và giả định “blocked transmission”**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **15.2 — Dùng ngôn ngữ thận trọng: estimated/prevented under assumptions, không claim causal tuyệt đối**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **15.3 — Báo cáo uncertainty cho random baseline và bootstrap CI cho deterministic strategies**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **15.4 — Kiểm tra selected_index_cases/selected_contacts để tránh chiến lược chỉ chọn toàn index case nếu mục tiêu là can thiệp contact**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 16: Mở rộng budget/cost setting

**Output bàn giao:** Budget curve + decision table  
**Owner đề xuất:** Experiment lead  
**Time estimate:** 2-3 days  
**Ghi chú:** Điểm mạnh hiện tại là decision under budget; nên khai thác sâu.  
**Priority note:** Paper value

**Subtasks & criteria**
- **16.1 — Ngoài k=1%, 5%, 10%, chạy curve nhiều mức k: 1-20% hoặc budget liên tục**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **16.2 — Thử cost-weighted intervention: cách ly/test/monitor có chi phí khác nhau**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **16.3 — Báo cáo area under intervention curve hoặc marginal gain per added node**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **16.4 — Viết khuyến nghị theo nguồn lực thay vì “một model luôn tốt nhất”**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 17: Bổ sung thống kê và uncertainty

**Output bàn giao:** Statistical analysis subsection + CI in tables/figures  
**Owner đề xuất:** Statistics lead  
**Time estimate:** 2 days  
**Ghi chú:** Reviewer tạp chí sẽ không chấp nhận chỉ báo cáo một seed duy nhất.  
**Priority note:** Submission strength

**Subtasks & criteria**
- **17.1 — Bootstrap 95% CI cho prevention rate, coverage, SIR reduction**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **17.2 — Permutation/randomization test khi so sánh GNN với baseline**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **17.3 — Báo cáo exact P value nếu dùng kiểm định**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **17.4 — Nêu số seed/fold rõ ràng trong Methods**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
