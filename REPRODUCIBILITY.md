# COSTTRACE Reproducibility Guide

## Environment

Validated with Python 3.13.9 on Windows. CPU execution is sufficient for validation and packaging. GPU support is optional through PyTorch and is not required for the commands below.

Install with pip:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Or with conda:

```bash
conda env create -f environment.yml
conda activate costtrace
```

## Configuration

Reviewer-facing settings live in `config/reproducibility.json`. Runtime path resolution lives in `src/costtrace/config.py`. The Phase 05 smoke and paper profiles are both declared in the JSON config.

## Validation Commands

```bash
python scripts/validate_paths.py
python scripts/validate_authoritative_artifacts.py
python scripts/validate_phase05_artifacts.py
python scripts/validate_paper_artifacts.py
python scripts/validate_reproducibility.py
pytest
python -m compileall main.py src scripts tests
```

Expected success markers:

- `PATH_VALIDATION_OK`
- `AUTHORITATIVE_ARTIFACTS_OK`
- `PHASE05_ARTIFACTS_OK`
- `PAPER_ARTIFACTS_OK`
- `REPRODUCIBILITY_OK`

## Pipeline Commands

Dry-run the complete pipeline wiring without rerunning experiments:

```bash
python main.py --phase all --dry-run
```

Run lightweight existing phases only when needed:

```bash
python main.py --phase prepare
python main.py --phase metrics
```

Do not run model training or paper-grade Phase 05 sweeps during routine validation unless a paper rerun is explicitly required.

## Expected Outputs

- Canonical processed SASHTS data under `data/processed/sashts/`
- Authoritative results under `results/metrics/`, `results/model/`, and `results/intervention/`
- Paper-ready figures and tables under `results/paper_ready/`
- Supplementary package index under `supplement/`

## Troubleshooting

- If imports fail, confirm `pip install -r requirements.txt` completed in the active environment.
- If artifact validators fail, check whether generated result folders were omitted from the checkout.
- If Phase 05 validation reports smoke-profile limitations, that is expected for fast validation; run the paper profile only for final manuscript estimates.
