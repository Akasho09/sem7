import pdfplumber
import pandas as pd

pdf_path = "norcet.pdf"   # change if needed
output_csv = "male_candidates_above_60.4172.csv"

rows = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        try:
            text = page.extract_text()
            if not text:
                continue
            for line in text.splitlines():
                parts = line.split()
                if len(parts) >= 6:
                    try:
                        gender = parts[-3]
                        percentage = float(parts[-2])
                        if gender.lower() == "male" and percentage >= 60.417:
                            rows.append(parts)
                    except:
                        continue
        except Exception as e:
            print(f"Skipping page {page_num}: {e}")

# Convert to DataFrame
df = pd.DataFrame(rows)

# Adjust column headers dynamically
max_cols = df.shape[1]
colnames = ["S.No","Roll No","Category","PWBD","Gender","Percentage","Rank"]
colnames = colnames[:max_cols] + [f"Extra{i}" for i in range(max_cols-len(colnames))]
df.columns = colnames

# Save to CSV
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"✅ Extraction complete. Saved {len(df)} rows to {output_csv}")
