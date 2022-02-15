from csv import DictReader, DictWriter

from util import COLUMN_NAMES

if __name__ == '__main__':
    with open('public-games.csv', 'r') as infile:
        with open('ranked.csv', 'w') as outfile:
            reader = DictReader(infile, fieldnames=COLUMN_NAMES)
            writer = DictWriter(outfile, fieldnames=COLUMN_NAMES)
            for row in reader:
                if row['game_type'] == 'ranked':
                    writer.writerow(row)
