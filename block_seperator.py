#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import os



def block_reader(file):
    entries = []
    
    line = file.readline()
    while line != "\n" and line !="":
        if "HEX" in line:
            line = line.split(":")[0]
            line = line.replace(" ","").replace("HEX","") #remove prefix
            entries.append(line)
        line = file.readline()
    return entries

def pack_blocks(key_array,offset):
    block_dir = []
    for key in key_array: 
        block_dir.append((key,offset))
    return block_dir

def write_to_file(output_file,pack_array):
    for pack in pack_array:
        output_file.write(pack[0]+","+pack[1]+"\n")


def file_handler(input_file_name, out_put_file_prefix):
    
    out_file_name = out_put_file_prefix+input_file_name.split("_")[0] + ".csv"
    
    f = open(input_file_name)
    of = open(out_file_name+"","w")

    line = f.readline()

    # counter = 5

    offset_array = []

    while line:
        if "Data Block #" in line:
            block_position = line.split("@")[1].replace(" ","").replace("\n","")
            block = block_reader(f)
            # offset_array.extend(pack_blocks(block,block_position))
            pack_array = pack_blocks(block,block_position)
            write_to_file(of,pack_array)
        line = f.readline()

    of.close()


if __name__ == "__main__":    
    DUMP_FILE_DIR="./"

    if len(sys.argv) > 1:
        DUMP_FILE_NAME = sys.argv[1]

    OUT_PUT_FILE_PREFIX = "key_distribution"
    if len(sys.argv) > 2:
        OUT_PUT_FILE_PREFIX = sys.argv[2]

    files = []

    for r, d, f in os.walk(DUMP_FILE_DIR):
        for file in f:
            if '.txt' in file:
                files.append(file)
    files.sort()

    for f in files:
        file_handler(f,OUT_PUT_FILE_PREFIX)



    # print block_reader(f)    
