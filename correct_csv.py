import re

# Open the input file for reading and the output file for writing
with open('TWEETS - kopie.csv', 'r', encoding="iso-8859-1") as f_in, open('output.txt', 'w',
                                                                          encoding="iso-8859-1") as f_out:
    # Read the file line by line
    for line in f_in:

        # Check if the line contains ",POSITIVE", ",NEGATIVE", or ",NEUTRAL"
        if ",POSITIVE" in line or ",NEGATIVE" in line or ",NEUTRAL" in line:

            # Extract the text before the sentiment label
            text_before = line.split(',', 1)[0]

            # Check if the text before the sentiment label contains any commas but not any quotes
            if re.match('^([^",]*,)+[^"]*$', text_before) and not text_before.startswith(
                    '"') and not text_before.endswith('"'):
                # If the text matches the pattern and doesn't already have quotes around it, wrap it with quotes
                stringBeforeWoutLineBreaks = text_before.strip("\n")
                line = line.replace(text_before, f'"{stringBeforeWoutLineBreaks}"')

        # Write the modified line to the output file
        f_out.write(line)
