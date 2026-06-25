# Phase 03 — Dataset, Preprocessing, Split Protocol & Leakage Audit

## Objective

Làm rõ dữ liệu SASHTS, preprocessing, graph construction và loại bỏ nguy cơ leakage trong evaluation.

## Why this phase matters

Nếu split/evaluation bị leakage hoặc dữ liệu mô tả không rõ, toàn bộ kết quả mô hình sẽ khó được chấp nhận.

## Checklist mapping

| ID | Checklist item | Output bàn giao | Owner | Time | Priority note |
|---:|---|---|---|---|---|
| 8 | Chuẩn hóa dữ liệu SASHTS | Dataset section + preprocessing flowchart | Data lead | 3h | Methods |
| 9 | Audit leakage và split protocol | Revised evaluation protocol + leakage audit table | Modeling lead | 1-2 days | Reviewer-critical |
| 23 | Ethics, privacy, and data availability | Ethics + Data Availability + AI disclosure text | Corresponding author | 1-2h | Submission compliance |
| 24 | Reporting checklist phù hợp | Reporting checklist completed | Writing/Modeling lead | 3-4h | Transparency |


## Phase-level criteria

- Dataset section mô tả nguồn, license/access, thời gian thu thập, sensor, biến chính, preprocessing và graph construction.
- Có preprocessing flowchart hoặc textual pipeline có thể tái lập.
- Không dùng node-level random split nếu household/component overlap gây leakage; ưu tiên household-level split hoặc leave-one-household-out.
- Có leakage audit table nêu nguy cơ, mitigation và residual risk.
- Có Ethics, Data Availability, AI disclosure và reporting checklist phù hợp.


## Detailed subtasks

### Checklist 8: Chuẩn hóa dữ liệu SASHTS

**Output bàn giao:** Dataset section + preprocessing flowchart  
**Owner đề xuất:** Data lead  
**Time estimate:** 3h  
**Ghi chú:** Dữ liệu hiện: 140,542 proximity events, 340 individuals, 542 aggregated edges.  
**Priority note:** Methods

**Subtasks & criteria**
- **8.1 — Viết rõ nguồn SASHTS, license/access, thời gian thu thập, sensor, biến chính**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **8.2 — Mô tả inclusion/exclusion: self-loop, pair aggregation, edge weight = total_duration_sec**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **8.3 — Nêu limitation: Klerksdorp thiếu timestamp thật; graph hiện gần như tách theo household**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **8.4 — Thêm Data Dictionary mapping vào supplement**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 9: Audit leakage và split protocol

**Output bàn giao:** Revised evaluation protocol + leakage audit table  
**Owner đề xuất:** Modeling lead  
**Time estimate:** 1-2 days  
**Ghi chú:** Hiện code stratified split theo node trong cùng graph; với household components nhỏ có rủi ro leakage cao.  
**Priority note:** Reviewer-critical

**Subtasks & criteria**
- **9.1 — Thay node-level random split bằng household-level split/leave-one-household-out hoặc site-level split**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **9.2 — Fit scaler chỉ trên train fold, không fit MinMaxScaler trên toàn bộ 340 node trước split**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **9.3 — Kiểm tra feature nào chỉ biết sau outcome; loại bỏ hoặc giải thích thời điểm quan sát**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **9.4 — Báo cáo rõ transductive vs inductive setting**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 23: Ethics, privacy, and data availability

**Output bàn giao:** Ethics + Data Availability + AI disclosure text  
**Owner đề xuất:** Corresponding author  
**Time estimate:** 1-2h  
**Ghi chú:** Nếu JTD/AME thật: họ yêu cầu ethical statement và data sharing statement cho original article.  
**Priority note:** Submission compliance

**Subtasks & criteria**
- **23.1 — Viết Ethics Statement: public/de-identified academic dataset, không can thiệp y tế thật**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **23.2 — Nêu Data Availability: raw data source, processed data/code availability, restrictions nếu có**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **23.3 — Nêu AI/tool usage nếu journal yêu cầu disclosure**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **23.4 — Bảo đảm không đưa thông tin nhận dạng cá nhân trong figures/tables**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.

### Checklist 24: Reporting checklist phù hợp

**Output bàn giao:** Reporting checklist completed  
**Owner đề xuất:** Writing/Modeling lead  
**Time estimate:** 3-4h  
**Ghi chú:** REFORMS có 32 câu hỏi/8 modules cho ML-based science; không thay thế guideline journal nếu journal bắt buộc form riêng.  
**Priority note:** Transparency

**Subtasks & criteria**
- **24.1 — Nếu bài là observational/prediction model: cân nhắc STROBE/TRIPOD theo guideline JTD chính thức**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **24.2 — Vì có ML model, điền thêm REFORMS checklist hoặc dùng như internal audit**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **24.3 — Với mỗi item, ghi section/page/line trong manuscript hoặc lý do không áp dụng**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.
- **24.4 — Đưa checklist vào supplementary nếu journal yêu cầu**
  - Criteria: output phải kiểm chứng được trong file/code/repo; không viết chung chung; không invent thông tin ngoài evidence.
  - Expected evidence: commit/file diff, generated artifact, table/figure/doc section hoặc TODO có lý do nếu chưa đủ input.


## Codex prompt for this phase

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

## Phase acceptance checklist

- [ ] All checklist IDs in this phase are addressed.
- [ ] Files changed are listed in the phase report.
- [ ] Outputs match the expected deliverables above.
- [ ] Validation commands or manual checks are documented.
- [ ] Any unresolved issue is moved to a TODO with owner and reason.
- [ ] No unrelated changes are mixed into this phase.
