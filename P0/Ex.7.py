# Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene.
# This fragment should be printed on the console. Then calculate the complement of this fragment
# by calling the seq_complement() function
from seq0 import *
print("-----| Exercise 7 |------")

FOLDER = "../session-04/"
FILENAME = "U5.txt"
lenght = 20
sequence = seq_read_fasta(FOLDER + FILENAME)


print("Gene:", FILENAME)
print("Frag", sequence[:lenght])
print("Comp", seq_complement(sequence[:lenght]))
# Implement the seq_complement(seq) function, that calculates a new sequence composed of the complement base of each of
# the original bases. The bases work in pairs. A and T are complement, as well as C and G. Therefore, the complement
# sequence of "ATTCG" is "TAAGC".
