import json
import csv

def save_csv(file_path, records):
    if not records:
        return
    
    fields = records[0].keys()

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

def save_json(file_path, records):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)

def save_text(file_path, text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

