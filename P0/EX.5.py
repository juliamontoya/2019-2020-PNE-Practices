from seq0 import *

print("-----| Exercise 5 |------")

FOLDER = "../Session-04/"
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene " + file, seq_count(sequence))

# Implement the seq_count(seq) function, that calculates the number of times all the bases appears on the sequence.
# It returns a dictionary with all the information. The keys of the dictionary are the bases: 'A', 'T', 'C' and 'G'
