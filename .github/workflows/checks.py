from collections import Counter
import deepl
import json
import os
import requests


def notify_exception(message: str):
    print(message)
    if os.environ["DISCORD_WEBHOOK_URL"]:
        data = {
            "content": message,
            "username": "dqx-custom-translations"
        }
        requests.post(
            url=os.environ["DISCORD_WEBHOOK_URL"],
            data=data
        )
    raise Exception(message)


def check_glossary():
    with open("csv/glossary.csv", "r", encoding="utf-8") as f:
        glossary = f.read().strip()

    ja_list = []
    for line in glossary.split("\n"):
        ja = line.split(",")[0]
        ja_list.append(ja)

    duplicates = [k for k, v in Counter(ja_list).items() if v > 1]
    if duplicates:
        notify_exception(f"Duplicates found in glossary. Culprits: {duplicates}")

    print("✔️  Glossary is good!")


def check_jsons():
    for file in os.listdir("json/"):
        with open(f"json/{file}", "r", encoding="utf-8") as f:
            print(f"Opening file {file} for JSON validation.")
            try:
                json.loads(f.read())
            except:
                notify_exception(f"File {file} did not pass JSON validation.")
        print(f"✔️  {file} is good!")


if __name__ == "__main__":
    check_glossary()
    check_jsons()
