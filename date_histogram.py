import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import fire
from datetime import date
from util import COLUMN_NAMES


def main(csvfile):
    matplotlib.style.use('seaborn')
    serie = pd.read_csv(csvfile, names=COLUMN_NAMES, usecols=['date'])['date'].map(date.fromisoformat)
    plt.figure(figsize=(16, 9))
    # sns.histplot(serie, bins=2)
    serie.hist(bins=(serie.max() - serie.min()).days//30)
    plt.savefig(f'date_histogram_{csvfile}.pdf')


if __name__ == '__main__':
    fire.Fire(main)
