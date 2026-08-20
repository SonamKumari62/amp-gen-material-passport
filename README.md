# AMP-GEN Material Passport — Principal's Residence

Take-home task for the AMP-GEN AI/ML Intern role.

## What this repo contains

- `output/passport_filled.xlsx` — AMP-GEN template populated for all **64 numbered BoQ line items**
- `output/passport.json` — same 64 records as JSON
- `output/visualization.png` — building-level material distribution by Material Category
- `output/building_meta.json` — Page 1 building metadata (Bonus B3)
- `src/ocr_pages.py` — OCR helper for the scanned PDF
- `src/build_passport.py` — converts validated extraction JSON into the provided Excel template
- `src/visualize.py` — creates the material-category chart
- `data/boq_validated.json` — visually validated extraction used for the submitted outputs
- `APPROACH.md` — methodology and limitations

The assessment PDF itself is **not included** in the repository. It was supplied as an assessment attachment; put a local copy at `data/source.pdf` if you want to rerun OCR.

## Run in under 5 minutes

### 1. Install

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
