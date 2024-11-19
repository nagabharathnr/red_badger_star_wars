1. Problem Statement
The challenge was three tasks:
a. Calculate the proportion of human vs non-human characters in the Star Wars universe (overall and per movie).
b. Rank species by their total screen time based on the number of dialogue lines or words spoken.
c. Visualize how species screen time which evolves across movies.

2. Approach
I broke this problem into smaller tasks and followed a structured data pipeline: data ingestion, processing, analysis, and visualization.

Task 1: Proportion of Human vs. Non-Human Characters
Data Source: Used the Star Wars API (SWAPI).

Steps:
Queried the API to fetch character information, including their species.
Queried species endpoints to map species names to characters.
Counted the number of characters belonging to the "Human" species vs all other species.
Grouped the data by movie to compute proportions per movie.

Task 2: Ranking Species by Screen Time
Data Source: Star Wars movie scripts dataset (kaggle text file).

Steps:
Parsed the text file to extract characters and their dialogue.
Mapped characters to species using data from SWAPI.
Counted the total words spoken by each species to rank them by screen time.

Task 3: Visualizing Screen Time Evolution
Steps:
Aggregated word counts for each species across movies.
Used Python’s visualization libraries to create charts showing the distribution of screen time for different species across films.

3. Tools and Libraries Used
pandas: For efficient data manipulation and analysis.
requests: To interact with the Star Wars API.
matplotlib: For creating static visualizations.
seaborn: For enhanced charts and plots.
Git: For version control and collaboration.
PyCharm: As the primary development environment.
GitHub: For code hosting and sharing the final solution.

4. Results
Attaching screenshots to this repo
