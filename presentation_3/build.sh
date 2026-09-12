#!/bin/sh
# Build vector figure, then resolve TikZ page coordinates in two main passes.
set -eu
cd -- "$(dirname -- "$0")"
mkdir -p build
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build assets/thermal_plot.tex > build/figure-pass.txt 2>&1; then
    tail -60 build/figure-pass.txt
    exit 1
fi
cp build/thermal_plot.pdf assets/thermal_plot.pdf
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build assets/measurement_sensitivity.tex > build/measurement-pass.txt 2>&1; then
    tail -60 build/measurement-pass.txt
    exit 1
fi
cp build/measurement_sensitivity.pdf assets/measurement_sensitivity.pdf
for pass in 1 2; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex > "build/pass-$pass.txt" 2>&1; then
        tail -60 "build/pass-$pass.txt"
        exit 1
    fi
done
cp build/main.pdf main.pdf
printf 'Built presentation_3/main.pdf.\n'
