# Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene.
# This fragment should be printed on the console.
# Then calculate the reverse of this fragment by calling the seq_reverse() function.
from seq0 import *

print("-----| Exercise 6 |------")

FOLDER = "../Session-04/"
filename = "U5.txt"
length_bases = 20
sequence = seq_read_fasta(FOLDER + filename)

print("Gene " + filename)
print("Frag:", sequence[:length_bases])
print("Rev:", seq_reverse(sequence[:length_bases]))
