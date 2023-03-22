import csv

# Open the input and output CSV files
import re

with open('output (2).csv', 'r', encoding='iso-8859-1') as f_in, open('output2.csv', 'w', newline='',
                                                                      encoding='iso-8859-1') as f_out:
    # Create a CSV reader and writer objects
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    # Loop over each row in the input CSV file
    for row in reader:

        # Search for the specified pattern in the row
        match_obj = re.search(
            r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\+\d{2}:\d{2},([^,]+)?,(POSITIVE|NEGATIVE|NEUTRAL)$', str(row))

        # If the pattern is found, remove the corresponding column
        if match_obj:
            print(5)
            del row[match_obj.start(1):match_obj.end(2)]

        # Write the modified row to the output CSV file
        writer.writerow(row)
