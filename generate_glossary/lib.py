import json
from pathlib import Path
import sys


def read_json_file(file):
    with open(file, encoding="utf-8") as json_data:
        return json.loads(json_data.read())


def merge_jsons(files: list):
    merged_changes = {}
    for file in files:
        json_content = read_json_file(file=file)
        for item in json_content:
            key, value = list(json_content[item].items())[0]
            merged_changes[key] = value

    return merged_changes


def delete_file_if_exists(file_path):
    path = Path(file_path)
    
    if path.exists() and path.is_file():
        try:
            path.unlink()
        except Exception as e:
            pass


def read_glossary(file: str):
    with open(file, "r", encoding="utf-8") as f:
        data = f.read().rstrip()
    
    return data.split("\n")


def sort_glossary(file: str):
    def key_len(text):
        text = text.split(",", 1)
        return len(text[0].encode("utf-8"))

    data = read_glossary(file)
    data.sort(key=lambda x:key_len(x), reverse=True)

    with open(file, "w+", encoding="utf-8") as f:
        f.write("\n".join(data))


def remove_duplicates(source_file: str, dest_file: str):
    # use set to track uniques
    seen = set()

    data = read_glossary(source_file)
    for line in data:
        key, value = line.split(",", 1)
        unique_record = (key, value)
        seen.add(unique_record)
    
    with open(dest_file, "a+") as f:
        for key, value in seen:
            f.write(f"{key},{value}\n")


def verify_csv_format(file: str):
    data = read_glossary(file)
    for record in data:
        try:
            key, value = record.split(',', 1)
        except ValueError:
            print(f'bad format: {key}')
            sys.exit(1)
