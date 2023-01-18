.PHONY: all
all: defs.tsv undef2.tsv

defs.tsv: src/js/*.js
	python search-function-var.py > defs.tsv

undef2.tsv: undef.txt
	python match-undef.py > undef2.tsv

undef.txt: src/js/*.js
	node_modules/.bin/eslint -f unix src/js/*.js | cat > undef.txt
