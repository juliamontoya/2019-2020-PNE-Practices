#We need to develop the function print_seqs(seq_list) that receives a list of sequences and prints their number in the list,
# their length and the sequence itself.
from seq01 import Seq


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(seqs):
    for sequence in seqs:
        print("Sequence ", seqs.index(sequence), ": (Length : ", sequence.len(), ")", sequence)


print_seqs(seq_list)