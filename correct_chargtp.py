import csv

with open('TWEETS - kopie - kopie.txt', 'r', encoding='iso-8859-1') as infile:
    with open('newCSV.txt', 'w', encoding='iso-8859-1') as out:
        for line in infile.read():
            if line != ";" or line != "\n":
                out.write(line)

