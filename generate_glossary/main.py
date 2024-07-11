import shutil
import re
from lib import (
    merge_jsons,
    delete_file_if_exists,
    sort_glossary,
    remove_duplicates,
    verify_csv_format
)
from ignore import IGNORE
from override import OVERRIDE
from player_names import PLAYER_NAMES


# this path must be updated to your dqx_translations/json/_lang/en directory. this is defaulted
# to where github actions expect it to be.
dqx_translations_path = "../dqx_translations/json/_lang/en"

# list of files that contain common DQX terms we want to capture in our glossary
game_dictionary = merge_jsons([
    f"{dqx_translations_path}/subPackage91Client.json",
    f"{dqx_translations_path}/eventTextSysQuestaClient.json",
    f"{dqx_translations_path}/subPackage05Client.json",
    f"{dqx_translations_path}/subPackage41Client.win32.json",
    f"{dqx_translations_path}/smldt_msg_pkg_STAGE_ID.win32.json",
    f"{dqx_translations_path}/smldt_msg_pkg_LOCATIONTITLE.win32.json",
    f"{dqx_translations_path}/subPackage02Client.win32.json",
    f"{dqx_translations_path}/smldt_msg_pkg_NPC_DB.win32.json",
    f"{dqx_translations_path}/subPackage68Client.win32.json",
    f"{dqx_translations_path}/smldt_msg_pkg_PC_SAVE_POPPOINT_NAME.win32.json",
    f"{dqx_translations_path}/subPackage127Client.win32.json",
    f"{dqx_translations_path}/subPackage128Client.win32.json",
    f"{dqx_translations_path}/subPackage61Client.win32.json",
    f"{dqx_translations_path}/subPackage40Client.win32.json",
    f"{dqx_translations_path}/subPackage12Client.win32.json",
])

glossary_path = ".\glossary.csv"
delete_file_if_exists(glossary_path)

for key, value in game_dictionary.items():
    # remove tags from string.
    re_pattern = r'<%.*?>'
    key = re.sub(re_pattern, '', key)
    value = re.sub(re_pattern, '', value)

    # strings that have newlines in them are not terms.
    if '\n' in key or '\n' in value:
        continue
    if key in IGNORE:
        continue
    if not value or not key:
        continue
    if value == " ":
        continue
    # strings with 。are not terms.
    if key.endswith("。"):
        continue
    # this is a partial phrase caused by the regex parsing removal of tags.
    if value.startswith("'"):
        continue
    # if string starts with a particle, it isn't a term.
    if key.startswith("は　"):
        continue
    # some key strings might equal their value counterpart, specifically in subPackage128Client.
    # this was to fix bazaar search functionality. ignore these if we see them. 
    if key == value:
        continue

    # in the event we want to override what's in weblate with what's in the glossary.
    override_value = OVERRIDE.get(key)
    if override_value:
        value = override_value

    with open("glossary.csv", "a+") as f:
        f.write(f"{key},{value}\n")

# write all of the override strings into the glossary, even if it's a duplicate.
# we may have some that aren't overrides, but new strings. we'll dedupe the glossary later.
for key in OVERRIDE:
    with open("glossary.csv", "a+") as f:
        f.write(f"{key},{OVERRIDE[key]}\n")

# write custom player name strings into the glossary. this is temporary until functionality
# exists in clarity to allow players to do this themselves.
for key in PLAYER_NAMES:
    with open("glossary.csv", "a+") as f:
        f.write(f"{key},{PLAYER_NAMES[key]}\n")

# clean glossary up by removing duplicates, sorting and verifying format.
remove_duplicates(glossary_path, "temp.csv")
shutil.move("temp.csv", glossary_path)
sort_glossary(glossary_path)
verify_csv_format(glossary_path)

# move glossary to csv directory
shutil.move(glossary_path, "../csv/")
print("Generated glossary moved to ../csv/glossary.csv")