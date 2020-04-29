# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.



filename = input("Enter filename: ")
try:
    file = open(filename)
except:
    print("error The filename that you entered is not existed")
    exit()


for line in file:
    line = line.upper()
    line = line.rtrip()
    print(line)
    

