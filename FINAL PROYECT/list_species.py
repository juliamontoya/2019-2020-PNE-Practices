import http.server
import socketserver
import termcolor
from pathlib import Path
import json
import http.client

PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'  # we will get json information
socketserver.TCPServer.allow_reuse_address = True   # This is for preventing the error: "Port already in use"


def info_species(ext):
    # connection = http.client.HTTPConnection(SERVER)     #connect with the server
    connection = http.client.HTTPConnection(SERVER)  # connect with the server
    try:
        connection.request("GET", ext)              #asking for connection
        termcolor.cprint(f"\n[*] CONNECTION SUCCESSFUL: {SERVER}:{PORT}\n", 'blue')
    except ConnectionRefusedError:
        termcolor.cprint(f"\n[!] CONNECTION REFUSED: {SERVER}:{PORT}\n", 'blue')
        exit()
    response = connection.getresponse()   #Read the response message from the server
    termcolor.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')#  Print the status line
    data = response.read().decode("utf-8")    #Read the response's body
    decoded = json.loads(data)       #form the JSON received

    return decoded
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'yellow') # Print the request line
        request_line = self.requestline.split(' ')
        path = request_line[1]
        #  used to delete the interrogation mark.
        files = path.split('?')                     #split separates the content from the '?'
        file_1 = files[0]                           # This is the content before interrogation mark.


        # reads index from the file
        import requests, sys

        server = "http://rest.ensembl.org"
        ext = "/info/assembly/homo_sapiens?"

        r = requests.get(server + ext, headers={"Content-Type": "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()

        decoded = r.json()
        print(repr(decoded))
