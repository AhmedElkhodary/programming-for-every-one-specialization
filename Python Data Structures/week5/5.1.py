#Write a program to read through the mbox-short.txt
#and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of
#those lines as the person who sent the mail. The program creates
#a Python dictionary that maps the sender's mail address to a count
#of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.



filename = input("enter the file name: ")

try:
    file = open(filename)
except:
    print("error, the file is not exist")
    exit()

names = list()
counts = dict()
bigcount = None
bigname = None

for line in file:
    if line.startswith("From "):
        small_list = line.split()
        counts[small_list[1]] = counts.get(small_list[1],0)+1

    

for name, count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count

print(bigname,bigcount)

