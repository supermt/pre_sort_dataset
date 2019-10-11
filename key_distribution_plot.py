#!/usr/bin/python

# import re
# import json
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import os
import sys


def plot_one_file(file_name, axe):
    f = open(file_name, "r")
    lines = f.readlines()

    axe.set_title(file_name)

    xs = []

    ys = []

    for line in lines:
        line = line.replace("\n", "")

        key, posi = line.split(",")

        x = long(key.ljust(48, '0'))
        xs.append(x)
        y = long(posi, 16)
        ys.append(y)

    axe.plot(xs, "b")
    ys.sort()
    axe.twinx().plot(ys, "r")


if __name__ == "__main__":

    DUMP_FILE_DIR = "./"

    files = []

    for r, d, f in os.walk(DUMP_FILE_DIR):
        for file in f:
            if '.csv' in file:
                files.append(file)
    files.sort()

    column = 4

    row = len(files) / column + 1

    fig = plt.figure()

    axes = fig.subplots(row, column, sharex='col', sharey=True)

    fig.text(0.5, 0.04, 'Entry Sequence', ha='center')
    fig.text(0.04, 0.5, 'Key Distribution',
             va='center', color="b", rotation="90")
    fig.text(0.96, 0.5, 'Ordered_Position',
             va='center', color="r", rotation="270")
    plt.xticks([])
    plt.yticks([])
    file_index = 0
    for axes_row in axes:
        for axe in axes_row:
            plot_one_file(files[file_index],axe)
            file_index += 1
            if file_index >= len(files):
                break
    plt.show()
