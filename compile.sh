#!/usr/bin/env bash

TARGET="${1}"
WHITELIST="
	article.tex
	poster.tex
	slides.tex
	"

if [[ "$TARGET" = "all" ]] || [[ "$TARGET" = "" ]]; then
	for ITER_TARGET in *.tex; do
		if [[ $WHITELIST =~ (^|[[:space:]])$ITER_TARGET($|[[:space:]]) ]];then
			ITER_TARGET=${ITER_TARGET%".tex"}
			./compile.sh "${ITER_TARGET}"
		fi
	done
else
	pdflatex -shell-escape "${TARGET}.tex" || { echo "Initial pdflatex failed"; exit $ERRCODE; }
	pythontex.py ${TARGET}.tex || exit 1
	pdflatex -shell-escape "${TARGET}.tex" || { echo "Post-PythonTeX pdflatex failed"; exit $ERRCODE; }
	if [[ "${TARGET}" = "slides" ]]; then
		biber "${TARGET}" || { echo "Biber failed"; exit $ERRCODE; }
	else
		bibtex "${TARGET}" || { echo "Bibtex failed"; exit $ERRCODE; }
	fi
	pdflatex -shell-escape "${TARGET}.tex" || { echo "Post-bibliography pdflatex failed"; exit $ERRCODE; }
	pdflatex -shell-escape "${TARGET}.tex" || { echo "Pdflatex failed"; exit $ERRCODE; }
	pdflatex -shell-escape "${TARGET}.tex"
fi
