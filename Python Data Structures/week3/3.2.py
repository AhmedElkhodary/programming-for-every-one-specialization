# a program that prompts for a file name, then opens that file and reads through the file,
#  looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

filename = input("Enter the filename: ")

try:
    file = open(filename)
except :
    print("error, the file name that you entered not existed")
    exit()
total = 0    
count = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        stpos = line.find(":") + 2
        snum = line[stpos:]
        inum = float(snum)

        total = total + inum
        count = count + 1
        
print("Average spam confidence:",total/count)

