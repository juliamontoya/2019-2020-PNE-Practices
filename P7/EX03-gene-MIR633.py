import http.client
import json
import termcolor

dict_genes = {"FRAT1": "ENSG00000165879",     #defining the dictionaries
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

SERVER = "rest.ensembl.org"   #server adress
ENDPOINT = "/sequence/id"
PARAMETERS = "/ENSG00000207552?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETERS
#method=GET

#PRINT THE CONNECTION INFO
print()
termcolor.cprint(f"Server: {SERVER}", "blue")
termcolor.cprint(f"URL: {URL}", "blue")

#connect with the server
connection = http.client.HTTPConnection(SERVER)

try:
    connection.request("GET", ENDPOINT + PARAMETERS)
except ConnectionRefusedError:   # If the connection fail we print an error message
    print("ERROR! Cannot connect to the Server")
    exit()

# Read the response message from the server
response = connection.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

# -- Read the response's body
data = response.read().decode("utf-8")   # It is necessary to decode the information

# -- Create a variable with the data,
# -- form the JSON received
gene = "MIR633"
info_api = json.loads(data)


#PRINTING THE CODE
termcolor.cprint("Gene: ", "green", end="")
print(gene)
termcolor.cprint("Description: ", "green", end="")
print(info_api["desc"])
termcolor.cprint("Bases: ", "green", end="")
print(info_api["seq"])
