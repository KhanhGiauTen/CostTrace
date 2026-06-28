# Runtime Notes

- Validation environment: Python 3.13.9.
- Supported OS assumptions: Windows 10/11, macOS, or Linux with Python and standard scientific Python wheels.
- CPU is sufficient for validation, artifact checks, table generation, and figure packaging.
- Optional GPU support is available through PyTorch, but PR 5 validation does not require CUDA.
- Full model training and paper-grade Phase 05 reruns are intentionally excluded from the default reproducibility checks.
- Lightweight validation should complete on a laptop-class machine.
