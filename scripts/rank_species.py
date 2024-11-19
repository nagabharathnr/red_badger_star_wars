import os
import pandas as pd
import re

# paths
data_path = r"A:/star_wars/red_badger_star_wars/data/input"
character_species_path = r"A:/star_wars/red_badger_star_wars/data/output/character_data.csv"

scripts_data = []

for filename in os.listdir(data_path):
    if filename.endswith(".txt") or filename.startswith("SW_"):
        file_path = os.path.join(data_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            # extracting the movie name
            movie = filename.split(".")[0]
            for line in file:
                # match the format: "line_number" "CHARACTER" "dialogue"
                match = re.match(r'^"\d+"\s+"([^"]+)"\s+"(.*)"$', line.strip())
                if match:
                    character, dialogue = match.groups()
                    scripts_data.append({
                        "movie": movie.strip(),
                        "character": character.strip(),
                        "dialogue": dialogue.strip()
                    })
                else:
                    print(f"Skipping line: {line.strip()}")

scripts_df = pd.DataFrame(scripts_data)

print("Parsed DataFrame Preview:")
print(scripts_df.head())
print("Columns:", scripts_df.columns)

# confirm whether DataFrame has the expected columns
if "character" not in scripts_df.columns or scripts_df.empty:
    raise ValueError("Parsing failed. Check script files or parsing logic.")

# loading the character-species mapping
character_species = pd.read_csv(character_species_path)

# normalizing the character names and species names to keep them consistent matching
scripts_df["character"] = scripts_df["character"].str.strip().str.lower()
character_species["Name"] = character_species["Name"].str.strip().str.lower()

# creating a mapping of characters to species
character_species_mapping = dict(zip(character_species["Name"], character_species["Species"]))

# mapping species to characters
scripts_df["Species"] = scripts_df["character"].map(character_species_mapping).fillna("Unknown")

# debugging to identify characters mapped to "Unknown"
unknown_characters = scripts_df[scripts_df["Species"] == "Unknown"]["character"].unique()
print("Characters mapped as 'Unknown':", unknown_characters)

scripts_df["word_count"] = scripts_df["dialogue"].str.split().apply(len)

# aggregating the total word counts by species
species_screen_time = (
    scripts_df.groupby("Species")["word_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# top 10 species by screen time
top_10_species = species_screen_time.head(10)

# saving the top 10 species to a CSV
top_10_species.to_csv(r"A:/star_wars/red_badger_star_wars/data/output/top_10_species_screen_time.csv", index=False)

print("Top 10 species by screen time:")
print(top_10_species)