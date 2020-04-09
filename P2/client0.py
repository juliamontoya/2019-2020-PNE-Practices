# Class for sending messages easily to the server


def seq_ping():
    print("OK")




class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)