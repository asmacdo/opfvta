#!/usr/bin/env bash

TARGET="${1}"
WHITELIST="
	article.tex
	poster.tex
	slides.tex
	"

if [ "$TARGET" = "all" ] || [ "$TARGET" = "" ]; then
	for ITER_TARGET in *.tex; do
		if [[ $WHITELIST =~ (^|[[:space:]])$ITER_TARGET($|[[:space:]]) ]];then
			ITER_TARGET=${ITER_TARGET%".tex"}
			./compile.sh ${ITER_TARGET}
		fi
	done
else
	pdflatex -shell-escape ${TARGET}.tex || die
	pythontex.py ${TARGET}.tex || die
	pdflatex -shell-escape ${TARGET}.tex || die
	bibtex ${TARGET} || die
	pdflatex -shell-escape ${TARGET}.tex || die
	pdflatex -shell-escape ${TARGET}.tex || die
	pdflatex -shell-escape ${TARGET}.tex || die
	pdflatex -shell-escape ${TARGET}.tex || die
fi
