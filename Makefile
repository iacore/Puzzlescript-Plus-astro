.PHONY: all
all: scripts/undef2.tsv scripts/defs.tsv

scripts/defs.tsv: scripts/search-function-var.py src/js/*.js
	python scripts/search-function-var.py > scripts/defs.tsv

scripts/undef2.tsv: scripts/match-undef.py scripts/undef.txt
	python scripts/match-undef.py > scripts/undef2.tsv

scripts/undef.txt: src/js/*.js
	node_modules/.bin/eslint -f unix src/js/*.js > scripts/undef.txt
