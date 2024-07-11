import json
import os
import sys


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
    check_jsons()
