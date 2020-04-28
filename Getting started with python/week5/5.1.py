# a program to prompt the user for hours
# and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5
# times the hourly rate for all hours worked above 40 hours


hours = input("Enter Hours:")
rat = input("Enter rate:")
try:
    hrs = float(hours)
    rate = float(rat)
    
except:
     hrs = -1
     rat = -1
if hrs > 40:
    print((40*rate) + ((hrs-40) * (1.5*rate))) 
elif hrs > 0:
    print(hrs * rate)
else:
    print("error input")
