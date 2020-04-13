from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# exercise 1 PING COMMAND
print("* Testing PING...")
print(c.talk("PING"))

# exercise 2 GET COMMAND
print("* Testing GET...")
for n in range(0,5):
    print("Gene", n, c.talk(f"GET {n}"))

sequence = c.talk("GET 0")
# exercise 3 INFO COMMAND
print("* Testing INFO...")
print(c.talk("INFO " + sequence))

# exercise 4 COMP COMMAND
print("* Testing COMP...")
print("COMP " + sequence)
print(c.talk("COMP " + sequence))

# exercise 5 REV COMMAND
print("* Testing REV...")
print("REV " + sequence)
print(c.talk("REV " + sequence))

# exercise 6 GENE COMMAND
print("* Testing GENE...")
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in list_names:
    print("GENE", file)
    print(c.talk("GENE " + file))

