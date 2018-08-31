#!/bin/bash

python3 ./src/prediction-validation.py -a ./input/actual.txt -p ./input/predicted.txt -w ./input/window.txt  -o ./output/comparison.txt
