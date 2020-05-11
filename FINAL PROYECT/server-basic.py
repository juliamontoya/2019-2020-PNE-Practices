import http.server                    #First of all we are going to import all the necessary libraries
import socketserver
import termcolor
from pathlib import Path
import json
import http.client


# ---------DEFINE THE SERVER'S PORT--------
PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'                  # we will get json information
socketserver.TCPServer.allow_reuse_address = True          # This is for preventing the error: "Port already in use"

# ------WE CREATE THE FUNCTION------
def info_species(ext):
    connection = http.client.HTTPConnection(SERVER)        # connect with the server
    try:
        connection.request("GET", ext)                      # asking for connection
        termcolor.cprint(f"\n[*] CONNECTION SUCCESSFUL: {SERVER}:{PORT}\n", 'magenta')
    except ConnectionRefusedError:
        termcolor.cprint(f"\n[!] CONNECTION REFUSED: {SERVER}:{PORT}\n", 'magenta')
        exit()
    response = connection.getresponse()                     # Read the response message from the server
    termcolor.cprint(f"Response received!: {response.status} {response.reason}\n", 'magenta')  # Print the status line
    data = response.read().decode("utf-8")    # Read the response's body
    decoded = json.loads(data)       # form the JSON received

    return decoded

# -----------------------------------------------------------------------------------------------------------------------
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        try:

            termcolor.cprint(self.requestline, 'yellow')   # Print the request line
            request_line = self.requestline.split(' ')
            path = request_line[1]
                                                         # used to delete the interrogation mark.
            files = path.split('?')                      # split separates the content from the '?'
            file_1 = files[0]                            # This is the content before interrogation mark.



                                                         # reads the index from the file
            contents = Path('Error.html').read_text()    # opens the error.html file
            code_status = 404                            # status code in network

            try:

                if file_1 == "/":                               # Opens the indexx.html file
                    contents = Path("indexx.html").read_text()  # Reads the index from the file
                    code_status = 200

        # -----PART 1: LIST OF SPECIES----

                elif file_1 == "/listSpecies":
                    PARAMS = "?content-type=application/json"
                    endpoint = "info/species"                                # this endpoint returns Ok
                    species = info_species(endpoint + PARAMS)["species"]     # we use the FUNCTION to read the content of the list
                    file_2 = files[1]                                        # Stores the information after the '?'
                    file_3 = file_2.split("=")[1]                            # Stores the information after the '='



                    try:
                        if file_3 == "":                         # if the limit if empty, our application will print all 267 species
                            contents = f"""
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <title>List of species</title>
                                            </head>
                                            <body style="background-color: ORCHID">
                                            <h1>LIST OF SPECIES IN THE BROWSER</h1>
                                            <a href="http://127.0.0.1:8080/">Main page</a> 
                                            <h2>List of Species</h2>
                                                <p>Total number of species is: 267 </p>
                                                <p>The limit you have selected is:{267}</p>
                                                 <p>The names of the species are:</p>
                                            """
                            code_status = 200
                            for element in species:    # We create a for to list all tipe of species when the limit is empty
                                contents += f"""<p> > {element["common_name"]} </p></body></html>"""

                        elif int(file_3) > 267:
                            contents = Path('Error.html').read_text()
                            code_status = 404

                        elif int(file_3) < 0:
                            contents = Path('Error.html').read_text()
                            code_status = 404


                        else:                      # Now the application will print the name of spècies selected in the limit.ex 10,11...
                            contents = f"""
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charsetv="utf-8">
                                                <title>List of species</title>
                                            </head>
                                            <body style="background-color: 	MEDIUMTURQUOISE">   
                                            <h1>LIST OF SPECIES IN THE BROWSER</h1>
                                            <a href="http://127.0.0.1:8080/">Main page</a> 
                                                <p>The total number of species in the ensembl is: 267 </p>
                                                <p>The limit you have selected is:{file_3}</p>
                                                <p>The names of the species are:</p>
                                            """

                            code_status = 200

                            for element in species[:int(file_3)]:    # We create a for to list all tipe of species when a specific limit is selected.
                                contents += f"""<p> > {element["common_name"]} </p></body></html>"""
                    except ValueError:
                        contents = Path('Error.html').read_text()
                        code_status = 404


        #------PART 2: KARYOTYOPE-------



                elif file_1 == "/karyotype":
                    PARAMS= "?content-type=application/json"
                    endpoint = "info/assembly/"                   #this endpoint returns Ok
                    file_2 = files[1]                             # Stores the information after the '?'
                    file_3 = file_2.split("=")[1]                 # Stores the information after the '?'
                    species = info_species(endpoint + file_3 + PARAMS)["karyotype"]


                                                 # the console will print the number of chromosomes of the specie selected in the limit
                    contents = f"""                             
                                        <!DOCTYPE html>
                                        <html lang="en">
                                        <head>
                                            <meta charset="utf-8">
                                            <title>List of species</title>
                                        </head>
                                        <body style="background-color: 	LAWNGREEN">
                                        <a href="http://127.0.0.1:8080/">Main page</a>    
                                        <h1>DIFFERENT KARYOTYPES</h1>
                                            
                                            <p>The name of the chromosomes are:</p>
                                        """

                    for element in species:
                        contents += f"""<p> > {element} </p></body></html>"""

                    code_status = 200

        # ---------PART 3: CHROMOSOME LENGTH------

                elif file_1 == "/chromosomeLength":
                    endpoint = "info/assembly/"
                    PARAMS = "?content-type=application/json"
                    file_2 = files[1]
                    file_3, file_4 = file_2.split("&")
                    specie = file_3.split("=")[1]
                    chromosome = file_4.split("=")[1]
                    species = info_species(endpoint + specie + PARAMS)["top_level_region"]


                    for option in species:
                        if option["coord_system"] == "chromosome":
                            if option["name"] == chromosome:
                                contents = f"""
                                                                <!DOCTYPE html>
                                                                <html lang="en">
                                                                <head>
                                                                    <meta charsetv="utf-8">
                                                                    <title>List of species</title>
                                                                </head>
                                                                <body style="background-color: 	MEDIUMTURQUOISE">   
                                                                <h1>CHROMOSOME LENGTHS</h1>
                                                                <a href="http://127.0.0.1:8080/">Main page</a>
                                                                    <p>The length of the Chromosome is: {option["length"]}</p>
                                                                 </body></html>"""

                    code_status = 200
                else:
                    contents = Path('Error.html').read_text()
                    code_status= 404

            except KeyError:
                contents = Path('Error.html').read_text()
                code_status = 404

        except KeyboardInterrupt:
            contents = Path('Error.html').read_text()
            code_status = 404


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
