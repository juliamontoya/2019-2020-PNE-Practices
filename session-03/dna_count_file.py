#EXERCISE 3:
#Write a program that opens the dna.txt file and calculates the total number of bases,
# and the number of the different bases
#You must use a loop for counting the bases, Suppose that the DNA files always contains correct sequences


filename = open('dna.txt', 'r')
text = filename.read()
filename.close()

count_A = 0
count_C = 0
count_T = 0
count_G = 0

print("Total length: ", len(text))

for i in text:
    if i == 'A':
        count_A = count_A + 1
    elif i == 'C':
        count_C = count_C + 1
    elif i == 'G':
        count_G = count_G + 1
    elif i == 'T':
        count_T = count_T + 1

print("A: ", count_A)
print("C: ", count_C)
print("G: ", count_G)
print("T: ", count_T)