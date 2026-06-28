# Configuration

`config/reproducibility.json` is the reviewer-facing configuration record for the current reproducibility package. It centralizes canonical paths, seeds, budget levels, Phase 05 parameter grids, strategy names, model settings, and runtime assumptions.

The Python path layer in `src/costtrace/config.py` remains the runtime source for resolved repository paths. When available, `phase05_config()` reads the Phase 05 profiles from this JSON file so validation and packaging use documented settings.
