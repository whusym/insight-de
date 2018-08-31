from functools import reduce
from argparse import ArgumentParser


def read_actual(path, idx):
    '''
    Helper function to read the actual results。

    path: the path to the prediction file.
    idx: index of each timestamp.
    '''
    with open(path, 'r') as inputs:
        actual_dict = {row.split('|')[1]: float(row.split('|')[2])
                       for row in inputs if int(row.split('|')[0]) == idx}
    return actual_dict

def read_predicted(path, idx, actual_dict):
    '''
    Helper function to read the predicted results

    path: the path to the prediction file.
    idx: index of each timestamp.
    '''
    try:
        with open(path, 'r') as predicted:
            price_diff_val_total, price_diff_quant_total = 0, 0
            for row in predicted:
                row = row[:-1]   # remove the newline char at the end of each line
                row = row.split('|')   # split the line into a list using pipe
                if int(row[0]) == idx and row[1] in actual_dict:
                    price_diff_val_total += abs(actual_dict[row[1]] - float(row[2]))
                    price_diff_quant_total += 1
    except:
        print ("Error occurred while reading the file for the predicted values. Please contact the administrator.")

    return (price_diff_val_total, price_diff_quant_total)

def division(window_pair):
    '''
    Helper function to get the result for each window by dividing the total diff by the count within.
    window_pair: a pair including the total number of the difference in a certain window, and the
    total number of predicted value.
    Returns a float value or 'NA' if the denominator is 0.
    '''
    if window_pair[1] != 0:
        res = str("{0:.2f}".format(window_pair[0] / window_pair[1]))
        return res
    else:
        return 'NA'


def main(actual_path, predict_path, window_path, output_path):
    '''
    Main pipeline.
    actual_path: path to the file with actual values.
    predict: path to the file with predicted values.
    window_path: path to the file containing the numerical window value.
    output_path: path to the file containing comparison value at each window.
    '''

    # Get the total number of time stamps
    try:
        with open(actual_path, 'r') as predict:
            for row in predict:
                row = row[:-1]   # remove the newline char at the end of each line
                row = row.split('|')   # split the line into a list using
                last_row = row[0]
        last_row = int(last_row)
    except:
        print ("Error occurred while reading the file for the actual values. Please contact the administrator.")

    # get the window number
    try:
        with open(window_path, 'r') as windowfile:
            window_num = windowfile.read()
            window_num = int(window_num)
    except:
        print ("Error occurred while reading the file for window numbers. Please contact the administrator.")



    # get a list of differences between actual and prediction at each time stamp
    print ('Reading the prediction file...')
    diff_list = [read_predicted(predict_path, i, read_actual(actual_path, i)) for i in range(1, last_row + 1)]
    # manipulate the diff_list and get the desired result in a certain window
    print ('Calculating the average error...')
    res = map(division, [reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), diff_list[i:i + window_num]) for i in range(last_row + 1 - window_num)])
    # write results
    print ('Writing results...')
    with open(output_path, 'w') as filewrite:
        counter = 1
        for row in res:
            filewrite.write('{}|{}|{}\n'.format(counter, str(counter + int(window_num) - 1), row))
            counter += 1
    print ('All done! Check the output file for results.')


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-a', '--actual', dest='actual_path', help='path to input file', required=True)
    parser.add_argument('-p', '--predict', dest='predict_path', help='path to predict file', required=True)
    parser.add_argument('-w', '--window', dest='window_path', help='path to window file', required=True)
    parser.add_argument('-o', '--output', dest='output_path', help='path to output file', default='./output/comparison.txt')
    args = parser.parse_args()

    main(args.actual_path, args.predict_path, args.window_path, args.output_path)
