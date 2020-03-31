import pathlib
#para el ejercicio 1, definiremos la función seq_ping
#The seq_ping() functions is just for testing. It prints the "OK" string on the console
def seq_ping():
    print("OK")

#Para el ejercicio 2, definiremos la funcion seq_read_fasta
#Implement the seq_read_fasta(filename) function. It should open a file, in FASTA format,
# and return a String with the DNA sequence. The head is removed, as well as the '\n' characters.
def seq_read_fasta(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body
#para el ejrcicio 3
#the seq_len(seq) function, that calculates the total number of bases in the sequence.
def seq_len(seq):
    return len(seq)  #longitud sequencia
#para el ejercicio 4
#seq_count_base(seq, base) function, that calculates the number of times the given base appears on the sequence.
def seq_count_base(seq, base):
    return seq.count(base)   #cuenta cuantas veces aparece la base
#para el ejercicio 5
#mplement the seq_count(seq) function, that calculates the number of times all the bases appears on the sequence.
# It returns a dictionary with all the information. The keys of the dictionary are the bases: 'A', 'T', 'C' and 'G'
def seq_count(seq):
    bases = ["A", "C", "T", "G"]
    count_bases = []
    for base in bases:
        count_bases.append(seq_count_base(seq, base))
    dictionary = dict(zip(bases, count_bases))
    return dictionary
#para el ejercicio 6
#Implement the seq_reverse(seq) function, that calculates the reverse of the given sequence.
# Imaging we have this sequence: "ATTCG". Its reverse is: "GCTTA"
def seq_reverse(seq):
    return seq[::-1]
