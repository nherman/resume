.PHONY: all

all:
	pandoc -H src/pdformat.tex versions/web_engineer.md -o versions/web_engineer.pdf