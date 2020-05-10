import http.client
import json
import socketserver
import requests
import sys
from pathlib import Path
import http.server
import self as self
import termcolor
from seq1 import *

# Define the Server's port
PORT = 8080
server = "https://rest.ensembl.org"
IP = "localhost"
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def html_folder(title, sub_tittle):
    main_message = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: lightpink;">
    <h1>{sub_tittle}</h1>
    """

    return main_message


final_message = f"""
    <a href="http://127.0.0.1:8080/">Main Page </a>
</body>
</html> """


def info_species(ext):
    r = requests.get(server + ext, headers={"Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    return decoded


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        contents = ""
        # Open the form1.html file
        # Read the indexx from the file

        if self.path == "/":
            contents = Path("indexx.html").read_text()
            self.send_response(200)

        elif "/listSpeciesPrueba" in self.path:
            h1 = "LIST OF SPECIES IN THE BROWSER"
            body = "list of species"
            contents = html_folder("list_species.py", h1, body)
            self.send_response(200)


        else:
            contents = Path("Error.html").read_text()
            self.send_response(404)

        # Define the content-type header:

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return
# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
