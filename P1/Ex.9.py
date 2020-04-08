from seq1 import Seq

print("-- Practice 1, Exercise 9 --")

folder = "../session-04/"
FILENAME =folder + "U5.txt"
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FILENAME)
print(f"Sequence : (Length: {s.len()}) {s}")
print("\tBases: ", s.count())
print("\tRev: ", s.reverse())
print("\tComp:", s.complement())