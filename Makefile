all: plots.py countplot_game_type.pdf countplot_komi.pdf countplot_handicap.pdf countplot_board_size.pdf

ranked.csv: ranked.py
	python3 $<

countplot_game_type.pdf: countplot.py public-games.csv
	python3 $< public-games.csv game_type

countplot_komi.pdf: countplot.py ranked.csv
	python3 $< ranked.csv komi --nolabel

countplot_handicap.pdf: countplot.py ranked.csv
	python3 $< ranked.csv handicap

countplot_board_size.pdf: countplot.py ranked.csv
	python3 $< ranked.csv board_size
