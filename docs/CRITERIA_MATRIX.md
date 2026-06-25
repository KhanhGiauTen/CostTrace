# Criteria Matrix by Phase and Subtask

Use this file to track micro-criteria while executing each phase.

## Phase 00 — Submission Scope & Compliance Gate

### 1. Xác nhận đích nộp

- **Deliverable:** Link guideline chính thức + quyết định article type + scope fit note
- **Owner:** Corresponding author
- **Estimate:** 1h
- **Status from checklist:** Needs confirmation
- **Micro-criteria:**
  - [ ] 1.1 Xác nhận JTD chính xác là tạp chí nào và lấy guideline/template mới nhất
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 1.2 Chốt article type: Original Article/Research Article hay hướng khác
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 1.3 Kiểm tra scope: bài về contact network, GNN và epidemic intervention có nằm trong phạm vi JTD không
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 1.4 Chốt reference style: theo JTD chính thức hay theo yêu cầu nội bộ trong template local
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Việc này phải xong trước khi sửa citation/format. Template local đang song ngữ, khác với JTD/AME quốc tế.

### 2. Title page theo mẫu JTD local

- **Deliverable:** File title page hoàn chỉnh theo Template Title Page_JTD.docx
- **Owner:** Writing lead
- **Estimate:** 1-2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 2.1 Điền tiêu đề tiếng Việt IN HOA và tiêu đề tiếng Anh IN HOA
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 2.2 Điền đầy đủ tác giả, affiliation, email
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 2.3 Chọn corresponding author, điện thoại, ORCID nếu có
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 2.4 Đảm bảo thông tin title page trùng với bản thảo cuối
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Dùng file local Template Title Page_JTD.docx làm mẫu gốc nếu chưa có guideline khác.

### 3. Đổi tiêu đề nghiên cứu

- **Deliverable:** Vietnamese title + English title đã chốt
- **Owner:** Writing lead
- **Estimate:** 1h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 3.1 Bỏ màu sắc đồ án/course project khỏi title
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 3.2 Tiêu đề 10-15 từ, nói rõ: budget-constrained intervention, epidemic contact networks, graph learning
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 3.3 Tránh claim quá rộng như adaptive/optimal nếu chưa chứng minh bằng nhiều dataset
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 3.4 Chuẩn bị 2-3 phương án title để chọn
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Gợi ý EN: Budget-Constrained Node Intervention in Household Epidemic Contact Networks Using Graph Learning

## Phase 01 — Manuscript Identity, Abstract, RQ & Paper Conversion

### 4. Viết lại Abstract/Tóm tắt

- **Deliverable:** Tóm tắt song ngữ + 4-6 keywords
- **Owner:** Writing lead
- **Estimate:** 2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 4.1 Tóm tắt tiếng Việt 150-250 từ theo template local
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 4.2 Abstract tiếng Anh theo cấu trúc Background, Objective, Methods, Results, Conclusions nếu JTD yêu cầu
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 4.3 Nêu số liệu chính: 340 nodes, 542 edges, 88 households, GraphSAGE test AUC 0.7669, AP 0.8995, GNN prevention 26.8%/49.0% ở k=5%/10%
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 4.4 Không dùng giọng văn đồ án hoặc cảm ơn giảng viên
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Nếu JTD/AME là đích thật: Original Article abstract 200-450 words, 3-5 keywords.

### 5. Tái cấu trúc manuscript

- **Deliverable:** Manuscript .docx nghiên cứu, không còn dạng báo cáo cuối kỳ
- **Owner:** Writing lead
- **Estimate:** 4-6h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 5.1 Xóa/di chuyển Preface, lời cảm ơn môn học, TOC, thông tin lớp học khỏi main manuscript
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 5.2 Chuyển sang cấu trúc paper: Introduction, Related Work, Methods, Experiments, Results, Discussion, Limitations, Conclusions
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 5.3 Thêm Acknowledgments, Author Contributions, Funding, Conflicts of Interest, Data Availability, Ethics Statement
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 5.4 Đưa pipeline/artifact dài sang Supplementary Appendix
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Report PDF hiện có 42 trang và còn dấu vết final project report.

### 6. Làm rõ novelty và research questions

- **Deliverable:** Contribution paragraph + RQ cuối Introduction
- **Owner:** PI/Writing lead
- **Estimate:** 2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 6.1 Viết 2-3 research questions có thể kiểm định
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 6.2 Chốt đóng góp: budget-constrained node selection, comparison against centrality baselines, dual evaluation by counterfactual + SIR
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 6.3 Phân biệt rõ với DeepTrace: không claim tái hiện DeepTrace, chỉ mở rộng sang intervention ranking
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 6.4 Nêu giới hạn từ đầu: proof-of-concept trên household contact network
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Reviewer sẽ hỏi novelty ngay, nên phải đặt trước Methods.

## Phase 02 — Related Work, Novelty Positioning & Citation Base

### 7. Cập nhật literature review

- **Deliverable:** Related Work mới + reference library sạch
- **Owner:** Literature lead
- **Estimate:** 4h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 7.1 Bổ sung nghiên cứu 2020-2026 về digital contact tracing, epidemic networks, GNN for public health, influence maximization/vaccination strategy
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 7.2 Trích dẫn GraphSAGE, GCN/GAT, NetShield/influence maximization, temporal contact networks
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 7.3 Kiểm tra citation nào không liên quan hoặc quá chung thì bỏ
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 7.4 Tạo bảng so sánh related work nếu cần
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Không chỉ dựa vào DeepTrace; cần khung nghiên cứu rộng hơn.

## Phase 03 — Dataset, Preprocessing, Split Protocol & Leakage Audit

### 8. Chuẩn hóa dữ liệu SASHTS

- **Deliverable:** Dataset section + preprocessing flowchart
- **Owner:** Data lead
- **Estimate:** 3h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 8.1 Viết rõ nguồn SASHTS, license/access, thời gian thu thập, sensor, biến chính
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 8.2 Mô tả inclusion/exclusion: self-loop, pair aggregation, edge weight = total_duration_sec
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 8.3 Nêu limitation: Klerksdorp thiếu timestamp thật; graph hiện gần như tách theo household
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 8.4 Thêm Data Dictionary mapping vào supplement
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Dữ liệu hiện: 140,542 proximity events, 340 individuals, 542 aggregated edges.

### 9. Audit leakage và split protocol

- **Deliverable:** Revised evaluation protocol + leakage audit table
- **Owner:** Modeling lead
- **Estimate:** 1-2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 9.1 Thay node-level random split bằng household-level split/leave-one-household-out hoặc site-level split
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 9.2 Fit scaler chỉ trên train fold, không fit MinMaxScaler trên toàn bộ 340 node trước split
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 9.3 Kiểm tra feature nào chỉ biết sau outcome; loại bỏ hoặc giải thích thời điểm quan sát
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 9.4 Báo cáo rõ transductive vs inductive setting
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Hiện code stratified split theo node trong cùng graph; với household components nhỏ có rủi ro leakage cao.

### 23. Ethics, privacy, and data availability

- **Deliverable:** Ethics + Data Availability + AI disclosure text
- **Owner:** Corresponding author
- **Estimate:** 1-2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 23.1 Viết Ethics Statement: public/de-identified academic dataset, không can thiệp y tế thật
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 23.2 Nêu Data Availability: raw data source, processed data/code availability, restrictions nếu có
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 23.3 Nêu AI/tool usage nếu journal yêu cầu disclosure
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 23.4 Bảo đảm không đưa thông tin nhận dạng cá nhân trong figures/tables
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Nếu JTD/AME thật: họ yêu cầu ethical statement và data sharing statement cho original article.

### 24. Reporting checklist phù hợp

- **Deliverable:** Reporting checklist completed
- **Owner:** Writing/Modeling lead
- **Estimate:** 3-4h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 24.1 Nếu bài là observational/prediction model: cân nhắc STROBE/TRIPOD theo guideline JTD chính thức
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 24.2 Vì có ML model, điền thêm REFORMS checklist hoặc dùng như internal audit
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 24.3 Với mỗi item, ghi section/page/line trong manuscript hoặc lý do không áp dụng
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 24.4 Đưa checklist vào supplementary nếu journal yêu cầu
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** REFORMS có 32 câu hỏi/8 modules cho ML-based science; không thay thế guideline journal nếu journal bắt buộc form riêng.

## Phase 04 — Modeling Fixes, Benchmarks & Ablation

### 10. Fix GraphSAGE overfitting

- **Deliverable:** GraphSAGE training script mới + metrics nhiều seed/fold
- **Owner:** Modeling lead
- **Estimate:** 2-3 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 10.1 Implement early stopping thật với patience, không chỉ lưu best epoch rồi chạy đủ 500 epochs
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 10.2 Tune hidden_dim, dropout, weight_decay, learning rate bằng validation trong CV
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 10.3 So sánh train/val/test gap qua nhiều seed
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 10.4 Calibrate probability scores và ưu tiên ranking metrics thay vì threshold-only classification
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 10.5 Cân nhắc GraphSAGE nhỏ hơn hoặc logistic/ridge baseline nếu dataset vẫn nhỏ
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Hiện train AUC 0.9914 vs test AUC 0.7669; report cũng ghi hyperparameter chưa khớp code.

### 11. Bổ sung model benchmark

- **Deliverable:** Benchmark table chính + supplementary full metrics
- **Owner:** Modeling lead
- **Estimate:** 3-5 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 11.1 Traditional ML: Logistic Regression, Random Forest/XGBoost, SVM nếu phù hợp
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 11.2 Network baselines: degree, weighted degree, betweenness, closeness, PageRank, k-core, eigenvector
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 11.3 GNN baselines: GCN, GAT, GraphSAGE variants, MLP-no-graph ablation
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 11.4 Intervention baselines: random, greedy influence maximization/NetShield/vaccination heuristic nếu triển khai được
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Cần chứng minh GNN hơn baseline mạnh, không chỉ hơn random/betweenness.

### 12. Thử nghiệm trên nhiều dataset

- **Deliverable:** Multi-dataset experiment table + dataset summary table
- **Owner:** Experiment lead
- **Estimate:** 5-10 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 12.1 Thêm ít nhất 2 dataset contact network khác: ví dụ SocioPatterns school/workplace/hospital hoặc dataset public phù hợp
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 12.2 Nếu không có nhãn infection thật, dùng synthetic infection trên empirical networks và tách rõ phần mô phỏng
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 12.3 Chạy cùng protocol trên từng dataset
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 12.4 Báo cáo cross-dataset generalization hoặc limitation nếu chỉ có SASHTS
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Một dataset 340 node là chưa đủ mạnh cho bài nghiên cứu hoàn chỉnh.

### 13. Ablation study

- **Deliverable:** Ablation table + short discussion
- **Owner:** Modeling lead
- **Estimate:** 2-3 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 13.1 No-graph MLP vs GraphSAGE
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 13.2 Remove metadata features
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 13.3 Remove centrality features
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 13.4 Unweighted vs weighted adjacency
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 13.5 Static vs temporal graph nếu có timestamp
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 13.6 With/without index-case-related features
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Ablation giúp trả lời GNN học gì thật sự.

## Phase 05 — SIR Sensitivity, Counterfactual Evaluation & Budget Curves

### 14. Sensitivity analysis cho SIR

- **Deliverable:** Sensitivity plots + SIR parameter table
- **Owner:** Simulation lead
- **Estimate:** 3-5 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 14.1 Chạy grid beta/gamma/T thay vì chỉ beta=0.25, gamma=0.10, T=30
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 14.2 Tăng Monte Carlo runs lên 500-1000 nếu runtime cho phép
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 14.3 Báo cáo mean, 95% CI và robustness ranking theo từng tham số
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 14.4 Cân nhắc SEIR hoặc recovery-aware intervention
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 14.5 Không vẽ curve tái dựng nếu không lưu time-series simulation thật
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Hiện chart_sir_baseline được reconstruct từ aggregate summary; cần tạo time-series thật cho paper.

### 15. Làm rõ counterfactual evaluation

- **Deliverable:** Counterfactual Methods + Results được viết lại
- **Owner:** Evaluation lead
- **Estimate:** 2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 15.1 Định nghĩa rõ transmission edge và giả định “blocked transmission”
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 15.2 Dùng ngôn ngữ thận trọng: estimated/prevented under assumptions, không claim causal tuyệt đối
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 15.3 Báo cáo uncertainty cho random baseline và bootstrap CI cho deterministic strategies
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 15.4 Kiểm tra selected_index_cases/selected_contacts để tránh chiến lược chỉ chọn toàn index case nếu mục tiêu là can thiệp contact
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Hiện GNN chọn 100% SARS+ và nhiều index cases; cần giải thích thời điểm can thiệp.

### 16. Mở rộng budget/cost setting

- **Deliverable:** Budget curve + decision table
- **Owner:** Experiment lead
- **Estimate:** 2-3 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 16.1 Ngoài k=1%, 5%, 10%, chạy curve nhiều mức k: 1-20% hoặc budget liên tục
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 16.2 Thử cost-weighted intervention: cách ly/test/monitor có chi phí khác nhau
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 16.3 Báo cáo area under intervention curve hoặc marginal gain per added node
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 16.4 Viết khuyến nghị theo nguồn lực thay vì “một model luôn tốt nhất”
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Điểm mạnh hiện tại là decision under budget; nên khai thác sâu.

### 17. Bổ sung thống kê và uncertainty

- **Deliverable:** Statistical analysis subsection + CI in tables/figures
- **Owner:** Statistics lead
- **Estimate:** 2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 17.1 Bootstrap 95% CI cho prevention rate, coverage, SIR reduction
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 17.2 Permutation/randomization test khi so sánh GNN với baseline
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 17.3 Báo cáo exact P value nếu dùng kiểm định
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 17.4 Nêu số seed/fold rõ ràng trong Methods
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Reviewer tạp chí sẽ không chấp nhận chỉ báo cáo một seed duy nhất.

## Phase 06 — Results Narrative, Figures, Tables & Consistency Audit

### 18. Regenerate figures bằng tiếng Anh

- **Deliverable:** Figure folder paper_ready/ + captions tiếng Anh
- **Owner:** Visualization lead
- **Estimate:** 1-2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 18.1 Sửa toàn bộ title, axis, legend, annotation trong notebooks/reporting sang tiếng Anh
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 18.2 Ưu tiên vector/SVG hoặc PNG 300-600 dpi
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 18.3 Dùng style thống nhất, không quá nhiều màu, font đọc được khi in grayscale
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 18.4 Figure caption trong manuscript phải tự đủ nghĩa và nêu n/sample/metric
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 18.5 Kiểm tra results/figures/topology/*.png đang còn tiếng Việt
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Một số visualization ngoài visualizations/ đã tiếng Anh; notebook figures vẫn còn tiếng Việt.

### 19. Chuẩn hóa bảng

- **Deliverable:** Main tables + supplementary tables
- **Owner:** Writing/Stats lead
- **Estimate:** 1-2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 19.1 Bảng Dataset, Model Performance, Intervention Results, Ablation, Sensitivity
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 19.2 Thêm n, metric definition, mean/CI, units
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 19.3 Caption bảng đặt đúng theo guideline JTD đã xác nhận
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 19.4 Không nhồi bảng quá lớn vào main text; đưa full table vào supplementary
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Nếu theo local checklist hiện có thì đang hướng APA 7; nếu JTD/AME thì cần Vancouver/JTD style.

### 20. Đồng bộ số liệu giữa code và report

- **Deliverable:** Consistency audit passed + generated manuscript tables
- **Owner:** Reproducibility lead
- **Estimate:** 1 day
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 20.1 Sửa mismatch tên artifact: report nhắc sir_results.csv nhưng repo có sir_intervention_results.csv
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 20.2 Sửa mismatch hyperparameters: code dropout 0.35/0.20, report ghi 0.40
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 20.3 Đảm bảo mọi số trong paper đọc từ results/* mới nhất
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 20.4 Tạo script generate_tables.py để xuất bảng manuscript từ CSV/JSON
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Đây là lỗi nhỏ nhưng reviewer/editor rất dễ bắt.

### 27. Main results narrative

- **Deliverable:** Results + Discussion rewritten around claims
- **Owner:** Writing/Stats lead
- **Estimate:** 3h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 27.1 Viết kết quả thành 3 thông điệp chính, không chỉ liệt kê bảng
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 27.2 Nhấn mạnh conditional recommendation: degree tốt ở k=1%, GNN tốt ở k=5/10%
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 27.3 Giải thích vì sao dynamic duration coverage của degree cao nhưng prevention/SIR chưa luôn cao
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 27.4 Tách observed result khỏi interpretation
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Dựa trên final_comparison.csv và final_strategy_summary.json hiện có.

### 28. Limitations and future work

- **Deliverable:** Limitations section thành thật và thuyết phục
- **Owner:** Writing lead
- **Estimate:** 2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 28.1 Nêu rõ small graph, household-only components, missing timestamps for Klerksdorp, single dataset, simplified SIR, potential leakage, no real deployment
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 28.2 Đề xuất temporal graph, recovery-aware intervention, multi-dataset validation, SEIR, online intervention system
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 28.3 Không biến future work thành phần thay thế cho experiment bắt buộc nếu claim quá mạnh
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Report hiện đã có limitations nhưng cần đưa về chuẩn paper và gắn với threats to validity.

## Phase 07 — Reproducibility, Testing & Supplementary Package

### 21. Reproducibility package

- **Deliverable:** Reproduction instructions + pinned environment
- **Owner:** Engineering lead
- **Estimate:** 2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 21.1 Pin version trong requirements.txt hoặc tạo environment.yml/pyproject
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 21.2 Thêm config YAML cho seed, beta/gamma, budget levels, dataset paths
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 21.3 Tạo Makefile hoặc run_all.ps1 để tái tạo toàn bộ kết quả
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 21.4 Thêm README paper reproduction: data download, run, expected outputs
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 21.5 Lưu commit hash/code version trong manuscript
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Hiện requirements chưa pin version; pipeline chạy được nhưng chưa đủ chuẩn reproducibility.

### 22. Testing và code quality

- **Deliverable:** tests/ + CI/local test command
- **Owner:** Engineering lead
- **Estimate:** 2-3 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 22.1 Thêm unit tests cho curation, graph construction, metrics, SIR probability, top-k selection
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 22.2 Thêm smoke test chạy pipeline trên sample nhỏ
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 22.3 Tránh hard-coded row counts nếu dataset version thay đổi; chuyển sang validation có thông báo rõ
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 22.4 Chuẩn hóa logging và CLI phase names trong README/report/main.py
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** main.py có phase notebooks; report lại nhắc reporting. Cần thống nhất.

### 29. Supplementary material

- **Deliverable:** Supplementary Appendix + GitHub/release package
- **Owner:** Reproducibility lead
- **Estimate:** 1-2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 29.1 Đưa full pipeline, feature encoding, hyperparameters, full result tables, extra figures, data dictionary mapping
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 29.2 Thêm model cards/config, random seeds, runtime, hardware
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 29.3 Đưa notebooks đã cleaned hoặc link GitHub release
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 29.4 Nếu dữ liệu không phân phối lại được, chỉ cung cấp script xử lý và hướng dẫn tải dữ liệu
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Appendix hiện có nhưng vẫn dạng đồ án; cần chuyển sang technical supplement.

## Phase 08 — Language, References, Cover Letter & Final Submission Gate

### 25. References và citation style

- **Deliverable:** Reference list final + citation audit
- **Owner:** Reference lead
- **Estimate:** 1 day
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 25.1 Xác nhận style cuối: JTD/AME dùng Vancouver; template/checklist local hiện hướng APA 7
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 25.2 Nếu theo APA 7: đổi [1], [2] sang (Author, Year) và sort A-Z
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 25.3 Nếu theo Vancouver: giữ số thứ tự nhưng format đúng NLM/Vancouver
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 25.4 Bổ sung DOI/URL cho nguồn dữ liệu, code, paper chính
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 25.5 Kiểm tra cite trong text khớp reference list
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Không sửa style citation trước khi xác nhận đúng JTD nào.

### 26. Language polishing

- **Deliverable:** Polished English manuscript + Vietnamese abstract if required
- **Owner:** Writing lead
- **Estimate:** 1-2 days
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 26.1 Viết toàn bộ main manuscript bằng tiếng Anh học thuật nếu tạp chí yêu cầu
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 26.2 Giữ title page/abstract tiếng Việt theo template local nếu bắt buộc
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 26.3 Xóa các câu “our team learned”, “course project”, “instructor” khỏi paper
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 26.4 Proofread thuật ngữ: contact network, intervention, transmission, prevention rate, calibration
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Bản REPORT_EN hiện là dịch từ báo cáo, chưa phải paper prose.

### 30. Cover letter

- **Deliverable:** Cover letter bản nộp
- **Owner:** Corresponding author
- **Estimate:** 2h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 30.1 Viết 1 trang: problem, novelty, dataset, main findings, why JTD readers care
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 30.2 Nêu article type, reporting checklist followed, data/code availability
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 30.3 Nêu bài chưa submit nơi khác và conflict/funding nếu có
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 30.4 Nếu dùng AI hỗ trợ writing, disclose theo policy journal nếu bắt buộc
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Cover letter nên viết sau khi manuscript và scope fit đã chắc.

### 31. Final format pass

- **Deliverable:** Submission-ready package
- **Owner:** Submission lead
- **Estimate:** 2-3h
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 31.1 Body font/line spacing/margins/page numbering/line numbers theo guideline đã xác nhận
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 31.2 Figure legends, tables, supplementary đặt đúng thứ tự
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 31.3 File .docx cuối cùng không còn track changes/comment thừa
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 31.4 Kiểm tra plagiarism/similarity nếu trường/tạp chí yêu cầu
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 31.5 Đặt tên file nộp rõ ràng: Manuscript, TitlePage, Figures, Supplementary, Checklist
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Chỉ làm sau khi nội dung nghiên cứu đã ổn; format sớm quá sẽ phải làm lại.

### 32. Internal pre-submission review

- **Deliverable:** Reviewer-style comments resolved + final sign-off
- **Owner:** Cả nhóm
- **Estimate:** 0.5-1 day
- **Status from checklist:** To do
- **Micro-criteria:**
  - [ ] 32.1 Một người không viết chính đọc như reviewer: câu hỏi nghiên cứu, method, result, limitation
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 32.2 Kiểm tra từng claim có bảng/hình/source chống lưng
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 32.3 Chạy lại pipeline từ clean state trước ngày nộp
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
  - [ ] 32.4 Soát lần cuối title page, author order, corresponding author, funding/conflict/ethics
    - Evidence required: exact file path, generated artifact, table/figure, script output, or written section.
    - Validation: check consistency with manuscript, repo artifacts, and phase objective.
- **Coordination note:** Đây là cổng cuối trước khi submit.

