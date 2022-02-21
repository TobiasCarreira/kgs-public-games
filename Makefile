all: plots.py countplot_game_type.pdf countplot_komi.pdf countplot_handicap.pdf countplot_board_size.pdf

ranked.csv: ranked.py
	python3 $<

aago_games.csv: aago_games.py
	python3 $<

countplot_game_type.pdf: countplot.py public-games.csv
	python3 $< public-games.csv game_type

countplot_komi.pdf: countplot.py ranked.csv
	python3 $< ranked.csv komi --nolabel

countplot_handicap.pdf: countplot.py ranked.csv
	python3 $< ranked.csv handicap

countplot_board_size.pdf: countplot.py ranked.csv
	python3 $< ranked.csv board_size

# TODO: countplot de result y reason

date_histogram_public_games.pdf: date_histogram.py public-games.csv
	python3 $< public-games.csv

date_histogram_ranked.pdf: date_histogram.py ranked.csv
	python3 $< ranked.csv

date_histogram_aago.pdf: date_histogram.py aago_games.csv
	python3 $< aago_games.csv
