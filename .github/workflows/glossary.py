

def read_glossary():
    with open("csv/glossary.csv", "r", encoding="utf-8") as f:
        data = f.read()
    
    return data.split("\n")


def sort_glossary():

    def key_len(text):
        text = text.split(",", 1)
        return len(text[0].encode("utf-8"))

    data = read_glossary()
    data.sort(key=lambda x:key_len(x), reverse=True)

    with open("csv/glossary.csv", "w+", encoding="utf-8") as f:
        f.write("\n".join(data))


def build_hiragana_glossary():
    data = read_glossary()
    
    new_list = []
    for record in data:
        ja = record.split(",", 1)[0]
        en = record.split(",", 1)[1]

        ordinal = ord(ja[0])

        # https://www.unicodepedia.com/groups/hiragana/
        # \u3041 - \u309F, or 12353 - 12447
        if ordinal in list(range(12353, 12447)):
            new_list.append(f"{ja},{en}")

    with open("csv/hiragana_glossary.csv", "w+", encoding="utf-8") as f:
        for item in new_list:
            f.write(f"{item}\n")


if __name__ == "__main__":
    sort_glossary()
    build_hiragana_glossary()
