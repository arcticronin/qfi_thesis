#!/bin/sh
# Build twice so that TikZ's remembered page coordinates are resolved.
set -eu
cd -- "$(dirname -- "$0")"
mkdir -p build
for pass in 1 2; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error \
        -output-directory=build main.tex > "build/pass-$pass.txt" 2>&1; then
        tail -60 "build/pass-$pass.txt"
        exit 1
    fi
done
cp build/main.pdf main.pdf
printf 'Built main.pdf (11 main slides and 4 backup slides).\n'
