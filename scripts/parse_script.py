import pandas as pd
import re

# Define the path to the text file
file_path = "A:/star_wars/red_badger_star_wars/data/input/SW_EpisodeVI.txt"

# Initialize a list to store parsed rows
data = []

# Read and parse the text file
with open(file_path, "r", encoding="utf-8") as file:
    for line in file.readlines():
        # Skip empty lines or the header
        if line.strip() and not line.startswith('"character"'):
            # Use regex to extract character and dialogue
            matches = re.findall(r'"(.*?)"', line)
            if len(matches) >= 2:  # Ensure there are at least character and dialogue
                character = matches[1].strip()
                dialogue = matches[2].strip()
                data.append({"character": character, "dialogue": dialogue})

# Convert the list of dictionaries to a DataFrame
scripts_df = pd.DataFrame(data)

# Display the first few rows to verify
print(scripts_df.head())

# Save to a CSV file for reuse
output_path = "A:/star_wars/red_badger_star_wars/data/output/processed_scripts.csv"
scripts_df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}!")
