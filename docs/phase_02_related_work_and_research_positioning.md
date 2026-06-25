# Phase 02 — Related Work, Novelty Positioning & Citation Base

## Objective

Nâng literature review từ mức báo cáo môn học lên mức bài nghiên cứu có khung học thuật và citation base sạch.

## Why this phase matters

Novelty của paper chỉ thuyết phục khi được đặt cạnh literature về digital contact tracing, epidemic networks, network intervention và GNN.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 7 | Cập nhật literature review | Related Work mới + reference library sạch | Literature lead | 4h | Research depth |


## Phase-level criteria

- Related Work bao phủ các nhóm nghiên cứu chính, không chỉ dựa vào DeepTrace.
- Mỗi nhóm literature có synthesis, gap và connection với COSTTRACE.
- Citation library sạch: không trùng, không sai metadata, không thiếu DOI/venue nếu có.
- Ưu tiên nguồn 2020–2026 nhưng không bỏ qua nền tảng kinh điển nếu cần.


## Detailed subtasks

### Checklist 7: Cập nhật literature review

**Output bàn giao:** Related Work mới + reference library sạch  
**Owner đề xuất:** Literature lead  
**Time estimate:** 4h  
**Ghi chú:** Không chỉ dựa vào DeepTrace; cần khung nghiên cứu rộng hơn.  
**Priority note:** Research depth

**Subtasks & criteria**
- **7.1 — Bổ sung nghiên cứu 2020-2026 về digital contact tracing, epidemic networks, GNN for public health, influence maximization/vaccination strategy**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **7.2 — Trích dẫn GraphSAGE, GCN/GAT, NetShield/influence maximization, temporal contact networks**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **7.3 — Kiểm tra citation nào không liên quan hoặc quá chung thì bỏ**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **7.4 — Tạo bảng so sánh related work nếu cần**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
