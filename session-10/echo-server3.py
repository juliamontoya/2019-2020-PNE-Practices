import socket

IP = "212.128.253.174"
PORT = 8083
count = 0
ip_client_list = []

#step1: creating the socket

ls= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



#step 2: bind the socket to the server's IP and PORT

ls.bind((IP, PORT))



#step 3 : convert this general socket into a listening socket
ls.listen()

print("server is configured!!")
while  count < 5:

    try:
        # step 4 (main loop) : wait for client to connect

        (cs, client_ip_port) = ls.accept()  #on the variable cs we have the socket to comunicate with the variable y en la otra el ip y port
    except KeyboardInterrupt:
        print("server is done!")
        ls.close()
        exit()
    else:
        # step 5 (main loop) : receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        count +=1

        print("CONNECTION",count)
        print(f"Receive message: {msg}")
        print("Client IP, PORT:",client_ip_port)

        ip_client_list.append(client_ip_port)

        #step 6 (mainloop) : send a response to the client

        response = f"ECHO: {msg}\n "
        cs.send(response.encode())
        cs.close()

for i, c in enumerate(ip_client_list):
    print(f"Client {i}: {c}")