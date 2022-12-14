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
        en = line.split(",")[1]

        if "," in en:
            notify_exception(f"{line} has an invalid character in English string. Glossary upload will fail.")

        if '"' in ja:
            notify_exception(f"{line} has invalid character in Japanese string. Glossary upload will fail.")

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


def check_glossary_upload():
    if not os.environ["DEEPL_API_KEY"]:
        return print("❓  Did not find DEEPL_API_KEY, so unable to test glossary upload.")

    translator = deepl.Translator(os.environ["DEEPL_API_KEY"])

    with open("csv/glossary.csv", "r", encoding="utf-8-sig") as g_csv:
        contents = g_csv.read()

    glossary_dict = {}
    for entry in contents.split("\n"):
        line = entry.split(",", 1)
        if line[0]:
            glossary_dict.update({line[0]: line[1]})

    try:
        glossary = translator.create_glossary(
            name="DQX Glossary", source_lang="ja", target_lang="en", entries=glossary_dict)
    except:
        notify_exception("Glossary did not update to DeepL successfully.")

    glossaries = translator.list_glossaries()
    for glossary in glossaries:
        translator.delete_glossary(glossary=glossary.glossary_id)

    return print("✔️  Glossary uploaded to DeepL successfully!")

if __name__ == "__main__":
    check_glossary()
    check_jsons()
    check_glossary_upload()
