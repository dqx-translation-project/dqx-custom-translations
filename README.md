# dqx_custom_translations

Houses custom, server-side text translation files for Dragon Quest X.

## ./csv/

| filename | description |
| -------- | ----------- |
| glossary.csv | This is generated from `./generate_glossary/main.py`, which merges specific game files from [dqx_translations](https://github.com/dqx-translation-project/dqx_translations/), `./generate_glossary/npc_names.py` and `./generate_glossary/override.py`. This glossary file is pulled down from [dqxclarity](https://github.com/dqx-translation-project/dqxclarity) to merge into a player's local sqlite database for replacing common Japanese words with their English counterparts for use in various translation calls.
| merge.xlsx | This is an export of a Google [spreadsheet](https://docs.google.com/spreadsheets/d/1DgHlj9c53UB9cr29mjjBDbtus5T_3GW2Z09mvs3G_J4)  we use for fixing dialogue that doesn't get handled well by machine translation. The tabs in here are used in [dqxclarity](https://github.com/dqx-translation-project/dqxclarity) to update the player's local sqlite database by inserting or replacing text so that when the strings are encountered, they are replaced with these fixed versions. This tends to cover full, one-off sentences with general dialogue, walkthrough text (seen in the command menu), quest text and text in the "story so far" screen.

## ./generate_glossary/

Script that is used to generate our glossary file, which dumps the output into `./csv/merge.xlsx`. This is run via GitHub Actions and run on every PR, which will create a new commit in your PR with the updated glossary.

## ./json/

Each of these files stores different string types found in the game. Instead of shoving them all into one file, we break them out so the strings found are easier to identify where they came from. These are strings that are only ever encountered server-side. Each of these files are downloaded to the player's computer through [dqxclarity](https://github.com/dqx-translation-project/dqxclarity) and imported into their local sqlite database.

| filename | description |
| -------- | ----------- |
| custom_combat_chat.json | These are messages sent by story NPCs that have joined your party and say different bits of flavor text in the party window.
| custom_concierge_mail_names.json | This is a mixture of default concierge names seen in player MyTowns as well as the sender's name when interacting with mail from a Postmaster.
| custom_corner_text.json | Text seen in the upper-right hand corner of the screen, specifically from NPC chatter (not Dracky announcements.)
| custom_episode_request_book.json | Used for the weekly quests found in the episode request book in v5.
| custom_lottery_prizes.json | Prize text seen when speaking to the lottery NPC. Just stores the item names themselves.
| custom_mail.json | All of the mail text that we've captured from in-game events and NPCs that send the player mail.
| custom_master_quests.json | Text seen from the weekly master quest NPCs.
| custom_npc_name_overrides.json | Used to fix NPC names in both the party window and their nameplates.
| custom_quest_rewards.json | When opening a quest in the quest window, these are the reward strings.
| custom_seminar_questions_answers.json | When speaking with the orange Slime that enters you into the seminar mini-game, these are the answer strings.
| custom_team_quests.json | When part of a team and opening the team quest window, these are the quest description strings on what to do for the quest.
| custom_tower_answers.json | These are the answer strings found when doing Mysterious Tower content.
| custom_trainee_logbook.json | Used in the trainee logbook weekly quests found in v6.

## contributing

If you see a new string that matches one of these categories, you are welcome to open a PR to help us add/maintain these lists. Typically, these strings are dumped into your `logs/custom_text.log` file while running [dqxclarity](https://github.com/dqx-translation-project/dqxclarity).

Open a pull request with your changes against the appropriate file and someone will get your changes reviewed and merged.
