import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Open the CSV file and read its contents
with open('C:/Users/vecer/Downloads/output.csv', newline='', encoding="iso-8859-1") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # Skip the header row
    rows = []
    for row in reader:
        # Convert the date string to a datetime object
        #date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S+%z')
        date = row[0]
        # Convert the mood score string to a float
        score = float(row[3])
        # Append the row as a tuple
        rows.append((date, row[2], score))

# Sort the rows by date
rows.sort(key=lambda x: x[0])

# Group the rows by mood
moods = {}
for row in rows:
    mood = row[1]
    if mood not in moods:
        moods[mood] = []
    moods[mood].append(row)

# Create a plot for each mood
for mood, rows in moods.items():
    # Extract the dates and scores for this mood
    dates = [row[0] for row in rows]
    scores = [row[2] for row in rows]
    # Create the plot
    plt.plot(dates, scores, label=mood)

# Add labels and legend to the plot
plt.xlabel('Date')
plt.ylabel('Mood Score')
plt.title('Mood Scores Over Time')
plt.legend()

# Show the plot
plt.show()
