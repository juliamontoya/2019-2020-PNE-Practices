import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.35"


while True:
    # -- Ask the user for the message
    msg_user = input("Type your message: ")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -- Establish the connection to the Server
    s.connect((IP, PORT))

    # -- Send the user message
    s.send(str.encode(str(msg_user)))

    # -- Close the socket
    s.close()