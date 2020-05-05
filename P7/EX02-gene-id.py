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

#printing the information
number_genes = list(dict_genes.keys())
genes = list(dict_genes.values())

#go through every gene in the dictionary

print("Dictionary of genes!!")
print("There are ", len(number_genes), "GENES in the dictionary")
sol = ""
for i in number_genes:
    n = number_genes.index(i)
    termcolor.cprint(n, "green", end="")
    print(" -->", str(genes[n]))
