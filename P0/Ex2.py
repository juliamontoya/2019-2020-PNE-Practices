#Write a python program for opening the U5.txt file and writing into the console the first 20 bases of the sequence

from seq0 import*
FILENAME = "U5.txt"
FOLDER ="../session-04/"
length_bases = 20
print("DNA file: ", FILENAME)
print("The first ", length_bases, "bases are:")
print(seq_read_fasta(FOLDER + FILENAME)[:length_bases])


