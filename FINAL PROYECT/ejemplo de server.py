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

        termcolor.cprint(self.requestline, 'yellow')   # Print the request line
        request_line = self.requestline.split(' ')
        path = request_line[1]
        #  used to delete the interrogation mark.
        files = path.split('?')                     #split separates the content from the '?'
        file_1 = files[0]                           # This is the content before interrogation mark.


        # reads index from the file
        #opens the error.html file
        contents = Path('Error.html').read_text()
        code_status = 404                           #status code in network

        # Open the indexx.html file
        # Read the index from the file
        if file_1 == "/":
            contents = Path("indexx.html").read_text()
            code_status = 200

        elif file_1 == "/listSpecies":
            ENDPOINT = "info/species"  #this endpoint returns Ok
            species = info_species(ENDPOINT + PARAMS)["species"]
            file_2 = files[1]      #almacena lo de despues de la interrogacion
            file_3 = file_2.split("=")[1]   #almacena lo de despues de la igualdad


            if file_3 == "":   #si está vacio el limit, va a imprimir todos los 267 nombres
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightgreen">
                                <h1>LIST OF SPECIES IN THE BROWSER</h1>
                                <h2>List of Species</h2>
                                    <p>Total number of species is: 267 </p>
                                    <p>The limit you have selected is:{267}</p>
                                     <p>The names of the species are:</p>
                                </body></html>
                                """
                code_status = 200
                for element in species:    #creamos un for para listar todos los tipos
                    contents += f"""<p> - {element["common_name"]} </p>"""

            elif int(file_3) > 267:
                contents = Path('Error.html').read_text()
                code_status = 404

            elif int(file_3) < 0:
                contents = Path('Error.html').read_text()
                code_status = 404





            else:      #nos lista los tipos de especies segun el limit que se introduzca, ej 10, 11...
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightgreen">
                                <body style="background-color: lightgreen">
                                <a href="http://127.0.0.1:8080/">Main page</a>    
                                <h1>LIST OF SPECIES IN THE BROWSER</h1>
                                    <p>The total number of species in the ensembl is: 267 </p>
                                    <p>The limit you have selected is:{file_3}</p>
                                    <p>The names of the species are:</p>
                                </body></html>
                                """

                code_status = 200

                for element in species[:int(file_3)]:
                    contents += f"""<p> - {element["common_name"]} </p>"""



        elif file_1 == "/karyotype":
            ENDPOINT = "info/assembly/"              #this endpoint returns Ok
            file_2 = files[1]  # almacena lo de despues de la interrogacion
            file_3 = file_2.split("=")[1]  # almacena lo de despues de la igualdad
            species = info_species(ENDPOINT + file_3 +
                                         "?content-type=application/json")["karyotype"]
            contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightgreen">
                                <body style="background-color: lightgreen">
                                <a href="http://127.0.0.1:8080/">Main page</a>    
                                <h1>DIFFERENT KARYOTYPES</h1>
                                    
                                    <p>The name of the chromosomes are:</p>
                                </body></html>
                                """
            for element in species:
                contents += f"""<p> · {element} </p>"""

            code_status = 200



        elif file_1 == "/chromosomeLength":

            code_status = 200

        self.send_response(code_status)

        # Define the content-type header:
        self.send_header('Content-Type', "text/html")
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))
        return


Handler = TestHandler
# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
