from seq0 import *  # Write a python program for calculating the total length of the 5 Genes: U5, ADA, FRAT1, FXN and U5. The program should call the seq_len() function
FOLDER = "../Session-04/"
file_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for name in file_names:
    print("The gene", name, "---> Length: ", seq_len(FOLDER + name + ".txt"))
# Implement the seq_len(seq) function, that calculates the total number of bases in the sequence.
# It should be written in the Seq0.py file
