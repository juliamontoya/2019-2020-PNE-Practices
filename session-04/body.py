
from pathlib import Path


# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")[1:]
string = " "
string = string.join(body).replace(" ", "")


print("Body of the ud.txt file : \n", string)