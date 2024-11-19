import matplotlib.pyplot as plt

from red_badger_star_wars.scripts.rank_species import scripts_df, top_10_species

# grouping the word counts by movie and species
species_movie_screen_time = (
    scripts_df.groupby(["movie", "Species"])["word_count"]
    .sum()
    .unstack(fill_value=0)
)

# filter for the top 10 species identified in previous code
top_10_species_names = top_10_species["Species"]
species_movie_screen_time_top10 = species_movie_screen_time[top_10_species_names]

# plotting screen time evolution
species_movie_screen_time_top10.plot(kind="line", figsize=(12, 8), marker="o")

# customize the plot
plt.title("Screen Time Evolution by Species Across Movies")
plt.xlabel("Movie")
plt.ylabel("Screen Time (Words)")
plt.legend(title="Species", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)

# save the plot to a file
plot_path = r"A:/star_wars/red_badger_star_wars/data/output/species_screen_time_visualization.png"
plt.tight_layout()
plt.savefig(plot_path)
print(f"Plot saved to: {plot_path}")

# displaying the plot
plt.show()