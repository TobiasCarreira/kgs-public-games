import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import fire

from util import COLUMN_NAMES


def main(csvfile, column_name, label=True):
    df = pd.read_csv(csvfile, names=COLUMN_NAMES, usecols=[column_name])
    plt.figure(figsize=(16, 9))
    ax = sns.countplot(x=df[column_name])
    if label:
        ax.bar_label(ax.containers[0], fmt='%1.2e', fontsize=12)
    ax.set_yscale("log")
    plt.savefig(f'countplot_{column_name}.pdf')


if __name__ == '__main__':
    fire.Fire(main)
