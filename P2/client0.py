# Class for sending messages easily to the server
import socket
import termcolor


def ping():
    print("OK!")


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

