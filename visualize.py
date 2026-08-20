"""Create the building-level material distribution chart."""
import argparse, json, os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default="output/passport.json")
    ap.add_argument("--out", default="output/visualization.png")
    args = ap.parse_args()

    with open(args.json, encoding="utf-8") as f:
        df = pd.DataFrame(json.load(f))
    counts = df["Material Category"].value_counts().sort_values()

    plt.figure(figsize=(10, 7))
    counts.plot(kind="barh")
    plt.xlabel("Number of BoQ line items")
    plt.ylabel("Material category")
    plt.title("Principal's Residence — Material Distribution by Category")
    plt.tight_layout()
    plt.savefig(args.out, dpi=180)
    plt.close()
    print(args.out)

if __name__ == "__main__":
    main()
