import http.client
import json
import termcolor
from seq1 import *


def percentages(seq):
    count = seq.count()
    length = seq.len()
    listvalues = list(count.values())
    listt = []
    for value in listvalues:
        listt.append(f"{value} {round(value / length * 100), 2}%")
    listkeys = list(count.keys())
    for n in listkeys:
        n_index = listkeys.index(n)
        termcolor.cprint(n, "blue", end="")
        print(" -->", str(listt[n_index]))


dict_genes = {"FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

for gene in dict_genes:
    number_genes= list(dict_genes.keys())
    genes = list(dict_genes.values())
    phrase = dict_genes[gene]

    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id"
    PARAMETERS = "/" + phrase + "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMETERS
    #method=GET

    #PRINT THE CONNECTION INFO
    print()
    termcolor.cprint(f"Server: {SERVER}", 'blue')
    termcolor.cprint(f"URL: {URL}", 'blue')


    connection = http.client.HTTPConnection(SERVER)

    try:
        connection.request("GET", ENDPOINT + PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

# -- Read the response message from the server
    response = connection.getresponse()

# -- Print the status line
    termcolor.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

# -- Read the response's body
    data = response.read().decode("utf-8")

    info_api = json.loads(data)

    termcolor.cprint("Gene: ", "green", end="")
    print(gene)
    termcolor.cprint("Description: ", "green", end="")
    print(info_api["desc"])
    sequence = info_api["seq"]
    s = Seq(sequence)
    termcolor.cprint("Total length: ", "green", end="")
    print(s.len())
    percentages(s)
    termcolor.cprint("Most frequent base: ", "green", end="")
    print(sequence)

