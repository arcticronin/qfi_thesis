#!/bin/sh
# Beamer overlays and all diagrams are native PDF/TikZ; no video player required.
set -eu
cd -- "$(dirname -- "$0")"
mkdir -p build
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build assets/thermal_plots.tex > build/thermal-pass.txt 2>&1; then
    tail -60 build/thermal-pass.txt
    exit 1
fi
cp build/thermal_plots.pdf assets/thermal_plots.pdf
for pass in 1 2; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex > "build/pass-$pass.txt" 2>&1; then
        tail -60 "build/pass-$pass.txt"
        exit 1
    fi
done
cp build/main.pdf main.pdf
printf 'Built presentation_4/main.pdf (17 main slides, 7-step overlay, 10 appendices).\n'
