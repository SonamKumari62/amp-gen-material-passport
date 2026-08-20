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
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Rebuild the passport

```bash
python src/build_passport.py --template AMP_Passport_Template.xlsx --records data/boq_validated.json --outdir output
```

### 3. Rebuild the visualization

```bash
python src/visualize.py --json output/passport.json --out output/visualization.png
```

### Optional: OCR the source PDF

Place the supplied scan at `data/source.pdf`, then:

```bash
python src/ocr_pages.py --pdf data/source.pdf --out data/ocr_text
```

## Extraction approach

The source is a scanned, dot-matrix BoQ with handwritten quantities. OCR was therefore treated as a **first-pass extraction tool**, not as ground truth. The numbered line items, quantities, units, DSR codes, and page-1 metadata were visually checked against the scan before the final JSON/Excel export.

The required GREEN fields were prioritized. AMBER mass/carbon fields were not attempted because reliable material quantities and cited EPD/LCA factors could not be established within the task window. GREY circularity/detachability/lifespan fields were left blank as instructed.

## Validation

- Numbered BoQ items extracted: **64 / 64**
- Passport records exported: **64**
- Example rows from the supplied template were retained.
- Composite numbered items containing multiple sub-items (for example reinforcement, shuttering, handles, and CI accessories) remain **one passport record** so the submitted count stays aligned with the 64 numbered BoQ items.
- Where the scan contains ambiguous/blank schedule information, the source notation such as `N.S.1.` is retained rather than invented.

## Bonuses

- [x] **B3 — building metadata**
- [ ] B1 — live deployment
- [ ] B2 — carbon / EPD
- [ ] B4 — video

## Time spent

**Update this line with the applicant's actual clock time before submission. Do not claim an estimated time as actual time.**

## Tools

Python, PyMuPDF, Tesseract OCR, Pillow, openpyxl, pandas, matplotlib, and LLM-assisted extraction/review.
