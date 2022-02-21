from csv import DictReader, DictWriter
import pandas as pd
from util import COLUMN_NAMES


def main():
    aago_kgs_users = pd.read_csv('aago_kgs_ogs.csv')['KGS']
    aago_kgs_users = list(aago_kgs_users[~aago_kgs_users.isnull()])
    with open('ranked.csv', 'r') as infile:
        with open('aago_games.csv', 'w') as outfile:
            reader = DictReader(infile, fieldnames=COLUMN_NAMES)
            writer = DictWriter(outfile, fieldnames=COLUMN_NAMES)
            for row in reader:
                if (row['black'] in aago_kgs_users) or (row['white'] in aago_kgs_users):
                    writer.writerow(row)


if __name__ == '__main__':
    main()
