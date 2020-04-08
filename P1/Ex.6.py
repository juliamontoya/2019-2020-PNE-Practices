from seq1 import Seq
# -- Create a Null sequence
seq_1 = Seq()

# -- Create a valid sequence
seq_2 = Seq("ACTGA")

# -- Create an invalid sequence
seq_3 = Seq("Invalid sequence")

print("Practice 1, Exercise 6")
BASES = ["A", "G", "T","C"]
print("Sequence 1:(length: ", seq_1.len(),")",seq_1)
print("Bases:", seq_1.count())
print("\nSequence 2: (length:", seq_2.len(), ")", seq_2)
print("Bases:", seq_2.count())
print("\nSequence 3: (length:", seq_3.len(), ")", seq_3)
print("Bases:", seq_3.count())