from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP =  "192.168.1.41"
PORT = 8081
FOLDER = "../session-04/"
filename = FOLDER + 'U5.txt'
s = Seq()
s.read_fasta(filename)

# -- Create a client object
c = Client(IP, PORT)

c.debug_talk("Sending the U5 Gene to the server..")
c.debug_talk(s)