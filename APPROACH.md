# APPROACH

## 1. Problem framing
The source was a 13-page scanned Bill of Quantities for the Principal's Residence, containing 64 numbered BoQ line items. The target was the supplied AMP-GEN Material Passport template. I treated the 64 numbered items as the unit of extraction, while retaining multiple sub-items inside a single numbered item where the source groups them together.

## 2. Tools and why
I used **PyMuPDF + Tesseract OCR** for the first-pass extraction because the PDF has no usable text layer and is a scanned/dot-matrix document. I used Python/openpyxl for deterministic Excel generation, JSON for machine-readable export, and pandas/matplotlib for the building-level material-category visualization. An LLM was used to help structure OCR output, classify material categories, and review descriptions.

## 3. What worked
OCR recovered the main descriptions, DSR 1989 codes, units, and most quantities. Because the scan contains handwritten quantities and OCR errors, I visually checked the page images before writing the final 64 records. The required GREEN fields were prioritized. Units were normalized according to the template conventions (cum, sqm, m, kg, nos); the special `10 Cubic decimetre` convention was converted to cubic metres.

## 4. What did not work / limitations
The source is noisy, and OCR sometimes confused digits, punctuation, and characters such as `1/2`, `:`, and `0/6`. Some source line items contain several sub-items under one numbered item, so their quantities are retained as slash-separated values instead of inventing a single number. Rate and amount fields were not populated where the scan did not provide a reliable value. AMBER carbon fields were left blank because credible source-specific EPD/LCA factors could not be established responsibly within the task window.

## 5. If I had two more weeks
I would build a layout-aware OCR pipeline with table/column detection, add confidence scores at field level, create a review UI for uncertain quantities, link DSR/SOR codes to a structured reference database, and add material-level mass/carbon estimation with cited Indian EPD/LCA sources. I would also add automated schema validation and tests for every exported record.
