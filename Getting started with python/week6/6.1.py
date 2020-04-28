# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay should be the normal rate for hours up to 40 and time-
# and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to
# do the computation of pay in a function called computepay() and use the function
# to do the computation. The function should return a value. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should use
# input to read a string and float() to convert the string to a number. Do not worry
# about error checking the user input unless you want to - you can assume the user
# types numbers properly. Do not name your variable sum or use the sum() function.

hours = input("Enter hours:")
rates = input("Enter rate:")

try:
    hour = float(hours)
    rate = float(rates)
except:
    hour = -1
    rate = -1

def computepay(h,r):
    if h > 40:
        result = (40 *rate) + ((hour-40) * (rate * 1.5))
        return result
    elif h <= 40:
        result = hour * rate
        return result

if (hour>0) & (rate>0) :
    print("Pay",computepay(hour, rate))
else:
    print("Error please enter valid value (numerical)")            
