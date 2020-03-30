import socket

IP = "212.128.253.128"
PORT = 8080

#WE CREATE THE SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ESTABLISHING THE CONNECTION WITH THE SERVER
s.connect((IP, PORT))

# send data to the server
s.send(str.encode("DEL 1 AL QUE NOS VAMOS"))

#receive data from the server
msg = s.recv(2000)
print("message from the server: \n")
print(msg.decode("utf-8"))

#closing the connection
s.close()
