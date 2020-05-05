import http.client
import json
import termcolor


SERVER = "rest.ensembl.org"   #server adress
ENDPOINT = "/info/ping"     #this endpoint returns Ok
PARAMETERS = "?content-type=application/json"    #we will get json information
URL = SERVER + ENDPOINT + PARAMETERS

#print the connection information
print()
termcolor.cprint(f"Server: {SERVER}", "blue")
termcolor.cprint(f"URL: {URL}", "blue")

connection = http.client.HTTPConnection(SERVER)   #connect with the server

try:
    connection.request("GET", ENDPOINT + PARAMETERS)
except ConnectionRefusedError:    #if the connection fails we will  print an error
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = connection.getresponse()
# .getresponse() method that returns the reponse information from the server

# -- Print the status line
termcolor.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

# -- Read the response's body
data = response.read().decode("utf-8")     # It is necessary to decode the information
print(data)
# -- Create a variable with the data,
# -- form the JSON received
info_api = json.loads(data)   # loads(). is a method from JSON library  (read JSON response)

print(info_api)
ping = info_api['ping']
print(ping)

if ping == 1:    # if the response is == 1 the server is OK!
    print("PING OK! The database is running!")
else:
    print("KA")
