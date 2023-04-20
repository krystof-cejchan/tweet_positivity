import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv("./csv input data/tweets final.csv", parse_dates=["date"])

# Split data into positive and negative
df_pos = df[df["mood"] == "POSITIVE"]
df_neg = df[df["mood"] == "NEGATIVE"]

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(12, 5))

# Plot positive data with light blue color
ax.plot(range(len(df_pos)), df_pos["score"].sort_values(), color="lightskyblue")

# Plot negative data with red color
ax.plot(range(len(df_neg)), df_neg["score"].sort_values(), color="red")

# Set x-tick labels and title
#ax.set_xticks(range(len(df)))
#ax.set_xticklabels(df["date"].sort_values().dt.date, rotation=45)
ax.set_xlabel("Date")
ax.set_ylabel("Score")
ax.set_title("Positive and Negative Scores")

# Add a legend
ax.legend(["Positive", "Negative"])

# Show the plot
plt.show()
