import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv("./soubory_data/tweets final.csv", parse_dates=["date"])

# Split data into positive and negative
df_pos = df[df["mood"] == "POSITIVE"]
df_neg = df[df["mood"] == "NEGATIVE"]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot positive data with light blue color and alpha of 0.3
ax1.plot(df_pos["date"].sort_values(), df_pos["score"].sort_values(), color="lightskyblue")

# Plot negative data with red color
ax2.plot(df_neg["date"].sort_values(), df_neg["score"].sort_values(), color="red")

# Set axis labels and title for the left plot
ax1.set_xlabel("Date")
ax1.set_ylabel("Score")
ax1.set_title("Positive Scores")

# Set axis labels and title for the right plot
ax2.set_xlabel("Date")
ax2.set_ylabel("Score")
ax2.set_title("Negative Scores")

# Show the plot
plt.show()
