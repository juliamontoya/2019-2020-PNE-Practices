#Write a python program for calculating the total length of the 5 Genes: U5, ADA, FRAT1, FXN and U5.
# The program should call the seq_len() function
from seq0 import*
FOLDER = "../session-04/"
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 3 |------")
for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene " + file + " ---> Length: ", seq_len(sequence))
