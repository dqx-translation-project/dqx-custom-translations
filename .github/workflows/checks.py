from collections import Counter
import json
import os
import sys



def check_glossary():
    with open("csv/glossary.csv", "r", encoding="utf-8") as f:
        glossary = f.read().strip()

    ja_list = []
    for line in glossary.split("\n"):
        ja = line.split(",")[0]
        ja_list.append(ja)

    if duplicates := [k for k, v in Counter(ja_list).items() if v > 1]:
        print(f"Duplicates found in glossary. Culprits:\n{duplicates}")
        sys.exit(1)

    print("✔️  Glossary is good!")


def check_jsons():
    for file in os.listdir("json/"):
        with open(f"json/{file}", "r", encoding="utf-8") as f:
            print(f"Opening file {file} for JSON validation.")
            try:
                json.loads(f.read())
            except:
                print(f"{file} did not pass JSON validation.")
                sys.exit(1)
        print(f"✔️  {file} is good!")


if __name__ == "__main__":
    check_glossary()
    check_jsons()
