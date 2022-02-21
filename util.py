import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ['date', 'white', 'white_rank', 'black', 'black_rank', 'revision', 'game_type', 'board_size', 'handicap', 'komi', 'approx_time', 'score']


def count_column(serie, column_name):
    ax = sns.countplot(x=serie)
    ax.bar_label(ax.containers[0], fmt='%1.2e', fontsize=12)
    ax.set_yscale("log")
    plt.savefig(f'countplot_{column_name}.pdf')
    plt.clf()
    plt.cla()


def score_to_result(score):
    if score in ['8193.5', '8194.0']:
        return 'no result'
    elif float(score) < 0.0:
        return 'white won'
    elif float(score) > 0.0:
        return 'black won'
    else:
        return 'tie'


def score_to_reason(score):
    if score in ['8192.5', '-8192.5']:
        return 'time'
    elif score in ['8193.0', '-8193.0']:
        return 'resign'
    elif score in ['8194.5', '-8194.5']:
        return 'forfeit'
    else:
        return 'points'
