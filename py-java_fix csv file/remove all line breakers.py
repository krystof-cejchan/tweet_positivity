import csv

# Open the input CSV file and output file
with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    # Create a CSV reader and writer
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in reader:
        # Replace any occurrences of \n with nothing in each field
        cleaned_row = [field.replace('\n', '') for field in row]
        # Write the cleaned row to the output file
        writer.writerow(cleaned_row)
