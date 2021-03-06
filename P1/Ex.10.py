#Write a python program that automatically calculate the answer to this question:

#hich is the most frequent base in each gene?
from seq0 import *

print("--Practice 1, Exercise 10--")

FOLDER = "../Session-04/"
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    dict_bases = seq_count(sequence)
    min_value = 0
    best_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            best_base = base

    print("Gene", file, " : Most frequent Base: ", best_base)