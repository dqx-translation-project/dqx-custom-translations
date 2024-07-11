# generate_glossary

Generates a glossary.csv file, which is then moved to the repo root's `csv` directory with overwrite.

## usage

```sh
python main.py
```

## github actions

Each new pull request will generate a new, generated glossary and commit it into the pull request.

The action can also be manually triggered if a change has been merged upstream in the dqx_translation repository.

This action is also triggered nightly to keep this process as automated as possible.

## explanation

### ignore.py

A dict of strings to ignore. Please provide a description as to why we're ignoring a string in the value.

### override.py

A dict of strings to add into the generated glossary. If the string exists from the source files in `dqx_translations`, it is overwritten with what's in this file.

> [!CAUTION]
> **Do not add player names into this file. This is to keep custom player names separate from real game terms.**

### player_names.py

A dict of player name strings to add into the generated glossary. 