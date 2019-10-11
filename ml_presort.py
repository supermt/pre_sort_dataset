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
    # ys.sort()
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

    fig,ax= plt.subplots()
    plot_one_file(files[0],ax)
    plt.show()
