with open("csv/glossary.csv", "r", encoding="utf-8") as f:
    data = f.read()

data = data.split("\n")

def key_len(text):
    text = text.split(",", 1)
    return len(text[0].encode("utf-8"))

data.sort(key=lambda x:key_len(x), reverse=True)

with open("csv/glossary.csv", "w+", encoding="utf-8") as f:
    f.write("\n".join(data))
