import os
import pandas as pd

# path to our Star Wars scripts input directory
data_path = r"A:/star_wars/red_badger_star_wars/data/input"

scripts_data = []

for filename in os.listdir(data_path):
    if filename.endswith(".txt") or filename.startswith("SW_"):
        file_path = os.path.join(data_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            # using filename to identify the movie
            movie = filename
            for line in file:
                if ":" in line:
                    character, dialogue = line.split(":", 1)
                    scripts_data.append({
                        "movie": movie,
                        "character": character.strip(),
                        "dialogue": dialogue.strip()
                    })

# dataFrame from the parsed data
scripts_df = pd.DataFrame(scripts_data)
print(scripts_df.head())

scripts_df.to_csv(r"A:/star_wars/red_badger_star_wars/data/output/star_wars_scripts.csv", index=False)