# Open the input file for reading and the output file for writing
import re

with open('output (2).csv', 'r', encoding='iso-8859-1') as f_in, open('output (5).csv', 'w',
                                                                      encoding='iso-8859-1') as f_out:
    # Read the input file line by line
    for line in f_in:

        # Replace any newline characters with a space
        line = line.replace('\n', ' ').replace('\r', '')

        # Write the modified line to the output file
        f_out.write(line)

        # Add a newline character at the end of each record
        if re.match(r'^.*,(0(\.\d+)?|1(\.0+)?)$', line):
            f_out.write('\n')
            print(1)
