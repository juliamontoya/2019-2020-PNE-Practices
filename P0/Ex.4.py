# Write a python program for calculating the number of each bases located on each of the five genes
from seq0 import*
FOLDER = "../session-04/"
base_list = ["A", "G", "T", "C"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 4 |------")
for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene" + file)
    for base in base_list:
        print(base, ":", seq_count_base(sequence, base))
# Implement the seq_count_base(seq, base) function, that calculates the number of times the given base
# appears on the sequence. It should be written in the Seq0.py file
