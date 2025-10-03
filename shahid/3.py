import pdfplumber
import pandas as pd
import re

pdf_path = "norcet.pdf"
students = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
            match = re.match(r"(.*)\s+(Male|Female)\s+(\d+)", line)
            if match:
                name, gender, rank = match.groups()
                rank = int(rank)
                if gender == "Male" and rank > 1500:
                    students.append({"Name": name.strip(), "Gender": gender, "Rank": rank})

# Convert to DataFrame
df = pd.DataFrame(students)

# Save to CSV
df.to_csv("filtered_male_students.csv", index=False)

print("Filtered data saved to filtered_male_students.csv")

