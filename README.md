# Insight Data Engineering Coding Challenge
## Table of Contents
1. [Introduction and Background](README.md#introduction)
1. [Challenge details](README.md#challenge-details)
1. [How to run](README.md#how-to-run)



## Introduction and background

This challenge assumes the author were a data engineer working at a financial institution that analyzes real-time stock market data. To determine the best trading strategy, the company's data scientists created a machine learning model to predict the future price of a stock every hour, and they want to test it on real-time stock data.

The task of the data engineer, is to help test how accurate their predictions are over time by comparing their predictions with newly arriving real-time stock prices.


## Challenge details

This repo reads two different files, one provides the actual value of each stock every hour and the second lists the predicted value of various stocks at a certain hour during the same time period. In this setting, they are in the `input` folder, users can also specify detailed paths in the `run.sh` bash file. In the input folder, there is also a `window.txt` file, which holds a single integer value denoting the window size (in hours) for calculating the `average error`.

The output file contains the `average error` by calculating the average difference between the actual stock prices and predicted values over a specified sliding time window. Users can find the results in the file `output/comparison.txt`. The path for output file can also be specified in `run.sh` bash file.


### Calculation
To compute the average error in a given time window, we find the absolute difference between the actual and predicted values of every matched stock and time pair, and call this result `error`. We then compute the average of all errors within a certain time window to get the `average error`.


### Input files

Lines in both input files, `actual.txt` and `predicted.txt`, are listed in chronological order. Both contain the following pipe-delimited fields:

* `time`: An integer greater than 0 designating the hour.
* `stock`: ID of a stock
* `price`: Price of a given stock at the given hour.

The file, `window.txt`, will contain one value (an integer greater than 0), specifying the size of the sliding window in hours.


### Output file

You must create an output file named `comparison.txt` where each line has the following pipe-delimited fields:

1. Starting hour time window
1. Ending hour time window
1. `average error` rounded off to 2 decimal places.


## How to run
To run this program, simply navigate to the folder of this repo on your local machine, and type `./run.sh`. The results will appear in the `output` folder once the process is over.

### Dependencies
- Python 3.6

You only need native Python to run this program. It should work in Python 3.5 and Python 3.7 also. To make sure you have Python 3 installed in your command line environment, simply type `python3` in the command line and check whether the Python environment is correctly loaded.
### Advanced
