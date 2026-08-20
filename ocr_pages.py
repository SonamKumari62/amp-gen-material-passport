"""
OCR helper for the scanned BoQ.
Run:
    python src/ocr_pages.py --pdf data/source.pdf --out data/ocr_text
"""
import argparse, os
import fitz
import pytesseract
from PIL import Image

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", default="data/ocr_text")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    doc = fitz.open(args.pdf)
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img, config="--psm 6")
        with open(os.path.join(args.out, f"page_{i:02d}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    print(f"OCR complete: {len(doc)} pages -> {args.out}")

if __name__ == "__main__":
    main()
