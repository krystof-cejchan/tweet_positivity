import csv

# Open the CSV file for reading
with open('TWEETS.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = []
    for row in reader:
        # Fix any text containing commas
        for i in range(len(row)):
            if ',' in row[i]:
                row[i] = '"' + row[i] + '"'
        rows.append(row)

# Open a new CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the updated rows to the new CSV file
    for row in rows:
        writer.writerow(row)
