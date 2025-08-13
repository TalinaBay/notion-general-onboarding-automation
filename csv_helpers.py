import csv
import os
from config import ONBOARDING_TASKS

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_onboardees_from_csv(in_filename, out_filename):
    in_filepath = os.path.join(DATA_DIR, in_filename)
    out_filepath = os.path.join(DATA_DIR, out_filename)

    data = []
    error_rows = []

    with open(in_filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        for row in reader:
            role = row["role"].strip().lower()

            if role in ONBOARDING_TASKS:
                data.append({
                    "onboardee_id": row["onboardee_id"].strip(),
                    "onboardee_name": row["onboardee_name"].strip(),
                    "dob": row["dob"].strip(),
                    "role": role
                })
            else:
                print(f"❗️ Warning: role '{role}' not found for onboardee '{row['onboardee_name']}'!")
                error_rows.append(row)

    # Append onboarded rows to the output file
    file_exists = os.path.isfile(out_filepath)
    with open(out_filepath, mode="a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for onboardee in data:
            writer.writerow(onboardee)

    # Write remaining rows back to the input file
    with open(in_filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in error_rows:
            writer.writerow(row)

    return data