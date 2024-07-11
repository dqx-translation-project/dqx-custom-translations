# a dict of keys to exclude from adding to the glossary.
# please include a reason as to why we're ignoring a string.
# ex: "こ": "Not a DQX term."

IGNORE = {
    "": "Blank string. We don't want to use this.",
    "・": "Not a DQX term.",
    "こ": "Not a DQX term.",
    "-": "Not a DQX term.",
    ",": "Not a DQX term.",
    "Ａ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｋ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｑ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｊ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "！": "Don't replace punctuation.",
    "？": "Don't replace punctuation.",
    "無効": "'Null' in Weblate.",
    "あ": "The letter A. We don't want to replace this.",
    "現": "'P.' in Weblate.",
    "草": "'Grass' in Weblate.",
    "仮": "'Temporary' string in Weblate.",
    "真": "'T.' in Weblate.",
    "偽": "'F.' in Weblate.",
    "階": "'F.' in Weblate.",
    "西": "'West' in Weblate.",
    "南": "'South' in Weblate.",
    "北": "'North' in Weblate.",
    "東": "'East' in Weblate.",
    "犬": "'Dog' in Weblate.",
    "主": "'Lord' in Weblate.",
    "月": "'Mn.' in Weblate.",
    "扉": "'Door' in Weblate.",
    "筒": "'Tube' in Weblate.",
}
