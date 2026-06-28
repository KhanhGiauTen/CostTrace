# Supplement Reproduction Instructions

1. Create the Python environment from `requirements.txt` or `environment.yml`.
2. Validate canonical paths:

```bash
python scripts/validate_paths.py
```

3. Validate authoritative artifacts:

```bash
python scripts/validate_authoritative_artifacts.py
```

4. Validate Phase 05 artifacts:

```bash
python scripts/validate_phase05_artifacts.py
```

5. Validate paper-ready artifacts:

```bash
python scripts/validate_paper_artifacts.py
```

6. Validate the complete reproducibility package:

```bash
python scripts/validate_reproducibility.py
pytest
```

The full pipeline wiring can be checked without rerunning experiments:

```bash
python main.py --phase all --dry-run
```
