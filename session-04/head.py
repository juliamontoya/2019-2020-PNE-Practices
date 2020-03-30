#exercise 3: Write a python program that opens the file RNU6_269P.txt and prints only its head

from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents.split("\n")[0]) #with this we only print the head of the file
