import argparse
import math
import statistics
import csv


def run():
    # input_dataset = open(args.input_file, "r")
    # output_file = open(args.output_file, "w")
    # name =args.output_file
    input_dataset = open('log_dataset.txt', "r")
    output_file = open('results.txt', "w")
    name ='results.txt'
    # output_file.write(
    #     "Time\tRMS-x\tRMS-y\tRMS-z\t" +
    #     "Mean-x\t Mean-y\t Mean-z\t " +
    #     "Max-x\t Max-y\t Max-z\t " +
    #     "Min-x\t Min-y\t Min-z\t " +
    #     "IQR-x\t IQR-y\t IQR-z\t " +
    #     "Variance-x\t Variance-y\t Variance-z\t " +
    #     "Std-x\tStd-y\t Std-z\t ")
    # output_file.close()
    output_file.write(
        "RMS-x,RMS-y,RMS-z," +
        "Mean-x,Mean-y,Mean-z," +
        "Max-x,Max-y,Max-z," +
        "Min-x,Min-y,Min-z," +
        "IQR-x,IQR-y,IQR-z," +
        "Var-x,Var-y,Var-z," +
        "Std-x,Std-y,Std-z\n")
    output_file.close()
    eje_x = []
    eje_y = []
    eje_z = []
    _time = []
    _svm = []
    lines_to_evaluate = 10
    #lines_to_evaluate = args.lines
    #activity = args.activity
    lines = input_dataset.readlines()
    number_of_lines = len(lines)
    print(number_of_lines)

    i = 0
    output_file = open('results.txt', "a")
    for line in lines[4:]:
        line = line.split(",", 7)[:4]
        #_time.append(float(line[0]))
        eje_x.append(float(line[1]))
        eje_y.append(float(line[2]))
        eje_z.append(float(line[3]))
        _svm.append(float(line[1]))
        _svm.append(float(line[2]))
        _svm.append(float(line[3]))
        svm = SVM(_svm)
        if(i % lines_to_evaluate == 0 and i != 0):
            _results(eje_x, eje_y, eje_z, _time, output_file)
            eje_x = []
            eje_y = []
            eje_z = []
            svm = []
           # _time = []
        i += 1
    output_file.close()

    with open(name, 'r') as infile, open("log_dataset.csv", 'w') as outfile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        writer = csv.writer(outfile)
        writer.writerows(lines)
    # for element in eje_x:
    #     print(element)
    listaz = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]
    # print(IQR(listaz))
    # print(variance(listaz))
    # print(skewness(listaz))
    # print(std(listaz))
    # print(mean_(listaz))
    # print(variance(listaz))
    # SVM(listaz)


def _results(eje_x, eje_y, eje_z, _time, output_file):
    # Results string
    #""+str(round(mean_(_time), 2)) +
    results = (
               ""+str(round(RMS(eje_x), 2)) +
               ","+str(round(RMS(eje_y), 2)) +
               ","+str(round(RMS(eje_z), 2)) +
               ","+str(round(mean_(eje_x), 2)) +
               ","+str(round(mean_(eje_y), 2)) +
               ","+str(round(mean_(eje_z), 2)) +
               ","+str(round(max(eje_x), 2)) +
               ","+str(round(max(eje_y), 2)) +
               ","+str(round(max(eje_z), 2)) +
               ","+str(round(min(eje_x), 2)) +
               ","+str(round(min(eje_y), 2)) +
               ","+str(round(min(eje_z), 2)) +
               ","+str(round(IQR(eje_x), 2)) +
               ","+str(round(IQR(eje_y), 2)) +
               ","+str(round(IQR(eje_z), 2)) +
               ","+str(round(variance(eje_x), 2)) +
               ","+str(round(variance(eje_y), 2)) +
               ","+str(round(variance(eje_z), 2)) +
               ","+str(round(std(eje_x), 2)) +
               ","+str(round(std(eje_y), 2)) +
               ","+str(round(std(eje_z), 2)))

    # Adds the results string into the results.txt file
    output_file.write(results + '\n')

    print(statistics.mean(eje_x))

# Mean


def mean_(list_):
    return sum(list_)/len(list_)

# Root mean square


def RMS(list_):
    mean_square = 0
    for element in list_:
        mean_square = mean_square + (float(element)*float(element))
    mean_square = mean_square/len(list_)

    return math.sqrt(mean_square)

# Interquartile range, using wikipedia formula (wolfram also)


def IQR(list_):
    iqr = 0
    list_.sort()
    length = len(list_)
    mod = length % 4
    n = (length - mod) / 4
    n = int(n)
    if(mod == 1):
        iqr = (0.75 * list_[3*n] + 0.25 * list_[3*n+1]) - \
            (0.25 * list_[n-1] + 0.75 * list_[n])
    elif (mod == 3):
        iqr = (0.25 * list_[3*n+1] + 0.75 * list_[3*n+2]) - \
            (0.75*list_[n] + 0.25 * list_[n+1])
    elif (length % 2 == 0):
        if(length/4 % 2 == 0):
            iqr = (list_[3*int(length/4)] + list_[3*int(length/4)-1]) / \
                2 - (list_[int(length/4)] + list_[int(length/4)-1])/2
        else:
            iqr = list_[3*int(math.ceil(length/4))-2] - \
                list_[int(math.ceil(length/4))-1]

    return iqr

# Variance


def variance(list_):
    # mean = sum(list_)/len(list_)
    mean = mean_(list_)
    return sum((xi - mean)**2 for xi in list_)/(len(list_)-1)

# Standard deviation


def std(list_):
    std = math.sqrt(variance(list_))
    return std

# skewness


def skewness(list_):
    mean = mean_(list_)
    return (sum((xi - mean)**3 for xi in list_)/(len(list_)-1))/(std(list_)**3)

# Single vector magnitude


def SVM(list_):
    svm = 0
    for element in list_:
        svm = svm + float(element)**2 
    svm = float(math.sqrt(svm))
    print(svm)
    return svm
 # argparse


def main():
    parser = argparse.ArgumentParser(
        description="Calculate features from selected dataset")
    parser.add_argument("-input", help="Dataset file",
                        dest="input_file", type=str, required=True)
    parser.add_argument("-output", help="Features values file",
                        dest="output_file", type=str, required=False, default="results.txt")
    parser.add_argument("-lines", help="Define the number of lines to calculate features",
                        dest="lines", type=check_positive, required=False, default=-1)
    # parser.add_argument("-activity", help="Define the activity of the dataset",
    #                     dest="activity", type=str, required=True, default=-1)

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

# check if the amount of lines is positive


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue


if __name__ == "__main__":
    main()
