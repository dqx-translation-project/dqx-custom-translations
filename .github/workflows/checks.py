from collections import Counter
import json
import os
import sys


def check_glossary():
    """Parses the glossary.csv file for problems. Fails if any found."""
    with open("csv/glossary.csv", "r", encoding="utf-8") as f:
        glossary = f.read().strip()

    ja_list = []
    for line in glossary.split("\n"):
        try:
            ja = line.split(",")[0]
            en = line.split(",")[1]
        except IndexError:
            print(f"❌  Did not find value for record: {ja}")
            sys.exit(1)

        ja_list.append(ja)

    if duplicates := [k for k, v in Counter(ja_list).items() if v > 1]:
        print(f"❌  Duplicates found in glossary. Culprits:\n{duplicates}")
        sys.exit(1)

    print("✔️  No glossary duplicates found!")


def check_jsons():
    """Checks jsons for any syntax issues."""
    for file in os.listdir("json/"):
        with open(f"json/{file}", "r", encoding="utf-8") as f:
            print(f"Opening file {file} to validate JSON.")
            try:
                json.loads(f.read())
            except:
                print(f"❌  {file} has invalid JSON.")
                sys.exit(1)

        print(f"✔️  {file} is valid JSON!")


if __name__ == "__main__":
    check_glossary()
    check_jsons()
