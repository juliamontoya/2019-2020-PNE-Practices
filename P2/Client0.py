

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def ping(self):
        print("OK")

