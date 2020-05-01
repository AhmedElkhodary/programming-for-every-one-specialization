# a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

filename = input("Enter filename: ")

try:
    file = open(filename)
except:
    print("filename is not exist")
    exit()

hours = dict()
for line in file:
    if line.startswith("From "):
         stpos = line.find(':')-2
         hour= line[stpos:stpos+2]
         hours[hour]=hours.get(hour,0)+1

lst = list()
for key, val in hours.items():
    newtup = (key,val)
    lst.append(newtup)

lst.sort()

for key , val in lst:
    print(key,val) 

    
#sorted([ (key,val) for key, val in hours.items() ])
#for key , val in hours.items():
#    print(key,val) 


       

        
            
        
