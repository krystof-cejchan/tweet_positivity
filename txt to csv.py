import csv

# Open the input and output files
with open('tweets_modified_cut_text w q.txt', 'r') as infile, open('tweets-modified-py-sc.csv', 'w', newline='') as outfile:

    # Create a CSV writer object
    writer = csv.writer(outfile)

    # Write the header row
    writer.writerow(['date', 'mood', 'score'])

    # Loop over the lines in the input file
    for line in infile:

        # Split the line into fields
        fields = line.strip().split(',')

        # Write the fields to the CSV file
        writer.writerow(fields)
