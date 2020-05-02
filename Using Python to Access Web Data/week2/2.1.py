import re
filename = "text.txt"

try:
   file = open(filename)

except:
    print("error, filename is not exist")
    exit()

sum = 0
count = 0

for line in file:
    line = line.rstrip()
    numbers_in_line = re.findall('[0-9]+',line)
    if len(numbers_in_line) == 0  : continue
    for num in numbers_in_line:
         count = count + 1
         sum = sum + int(num)

print("There are ",count, "values and the sum ends with ",sum)
