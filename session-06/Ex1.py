#Modify the __ini__ methond of the Seq class so that it detects that the given string only have these four valid bases:
# 'A', 'C', 'G' and 'T'. If a different character is found, the sequence should be initilalized with the "ERROR" string,
# and the message "INCORRECT Sequence detected" printed on the console

class Seq:
    def __init__(self, strbases):
        v = True
        for i in strbases:
            if i != "A" and i != "C" and i != "G" and\
                    i != "T":
                v = False

        if v == True:
            self.strbases = strbases

        else:
            strbases = "ERROR"
            self.strbases = strbases
            print("ERROR!!")


    print("New sequence created!")

    def __str__(self):
        return self.strbases




pass


#-- Main program
s1 = Seq("AACGTC")
s2 = Seq("Hello? am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")



