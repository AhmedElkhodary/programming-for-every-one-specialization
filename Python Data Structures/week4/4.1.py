# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in
# the list and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order



fname = input("Enter file name: ")
try:
    file = open(fname)
except:
    print("error the file is not existed")
    exit()
big_list = list()
for line in file:
    small_list = line.split()
    for word in small_list:
         if word in big_list:
             continue
         big_list.append(word)

big_list.sort()
print(big_list)
                     
