# CostTrace

CostTrace là một pipeline phân tích mạng dịch tễ cho bài toán can thiệp có ràng buộc ngân sách. Dự án dùng dữ liệu SASHTS, xây dựng đồ thị tiếp xúc theo hộ gia đình, chấm điểm rủi ro node bằng chỉ số mạng và GraphSAGE proxy, sau đó so sánh các chiến lược chọn node dưới ngân sách 1%, 5% và 10%.

## Mục tiêu nghiên cứu

- Chuẩn hóa dữ liệu tiếp xúc thành đồ thị có trọng số theo thời lượng tương tác.
- Định lượng vai trò node bằng topology, centrality, community và đặc trưng dịch tễ.
- Huấn luyện mô hình GraphSAGE nhẹ để xếp hạng nguy cơ nhiễm.
- Đánh giá can thiệp bằng top-k allocation, counterfactual transmission và mô phỏng SIR.
- Xuất notebook/figure để hỗ trợ báo cáo cuối kỳ.

## Cấu trúc

```text
CostTrace/
  data/
    raw/                 dữ liệu SASHTS gốc và mô tả nguồn
    processed/           edge list, node list, graph object và tóm tắt EDA
  src/costtrace/
    preparation/         kiểm định, làm sạch, dựng đồ thị, hồ sơ dữ liệu
    analysis/            topology, centrality, community, tổng hợp điểm rủi ro
    modeling/            GraphSAGE proxy cho dự báo nguy cơ node
    intervention/        phân bổ ngân sách, counterfactual, SIR, tổng hợp kết quả
    reporting/           sinh notebook và figure báo cáo
  notebooks/             assessment, topology, intervention
  results/               bảng kết quả, metric và hình báo cáo
  models/                trọng số và metadata mô hình
  main.py                entrypoint chạy pipeline
```

## Cài đặt

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Chạy pipeline

```powershell
python main.py --phase prepare
python main.py --phase metrics
python main.py --phase model
python main.py --phase budget
python main.py --phase notebooks
```

Chạy toàn bộ:

```powershell
python main.py --phase all
```

## Artifact chính

- `results/final_comparison.csv`: bảng so sánh chiến lược theo ngân sách.
- `results/final_strategy_summary.json`: chiến lược tốt nhất ở từng mức ngân sách.
- `results/gnn_metrics.json`: chỉ số train/validation/test của GraphSAGE proxy.
- `notebooks/assessment.ipynb`: đánh giá theo rubric và checklist cuối kỳ.
- `notebooks/topology.ipynb`: cấu trúc mạng, component, centrality và community.
- `notebooks/intervention.ipynb`: so sánh chiến lược, mô hình và khuyến nghị ngân sách.

## Tài liệu tham khảo

- Hamilton, W. L., Ying, R., & Leskovec, J. (2017). Inductive representation learning on large graphs. *NeurIPS*.
- Kiss, I. Z., Miller, J. C., & Simon, P. L. (2017). *Mathematics of Epidemics on Networks*. Springer.
- Tan, C. W., Yu, P. D., Chen, S., & Poor, H. V. (2025). DeepTrace: Learning to Optimize Contact Tracing in Epidemic Networks with Graph Neural Networks.
