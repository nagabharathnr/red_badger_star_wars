import requests
import pandas as pd

# getting the character data from API
base_url = "https://swapi.dev/api"
characters = []
next_url = f"{base_url}/people/"

while next_url:
    response = requests.get(next_url)
    data = response.json()
    characters.extend(data['results'])
    next_url = data['next']

# determining the species and non-humans
species_mapping = {}
for char in characters:
    species_urls = char['species']
    if species_urls:
        species_url = species_urls[0]
        if species_url not in species_mapping:
            species_data = requests.get(species_url).json()
            species_mapping[species_url] = species_data['name']

# categorizing the characters into humans and non-humans
human_count, non_human_count = 0, 0
character_data = []

for char in characters:
    species = species_mapping.get(char['species'][0], 'Unknown') if char['species'] else 'Unknown'
    category = "Human" if species == "Human" else "Non-Human"
    character_data.append({
        "Name": char['name'],
        "Species": species,
        "Category": category
    })
    if category == "Human":
        human_count += 1
    else:
        non_human_count += 1

# finding the proportions
total = human_count + non_human_count
proportions = {
    "Category": ["Human", "Non-Human"],
    "Count": [human_count, non_human_count],
    "Proportion": [human_count / total, non_human_count / total]
}

output_dir = r"A:/star_wars/red_badger_star_wars/data/output"
character_df = pd.DataFrame(character_data)
proportions_df = pd.DataFrame(proportions)

character_df.to_csv(f"{output_dir}\\character_data.csv", index=False)
proportions_df.to_csv(f"{output_dir}\\proportions_data.csv", index=False)

print(f"Data saved to {output_dir}")

print(f"Human: {human_count / total:.2%}, Non-Human: {non_human_count / total:.2%}")