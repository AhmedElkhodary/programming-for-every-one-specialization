# a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error.
#If the score is between 0.0 and 1.0,
#print a grade using the following table:
#Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6  F


score = input("Enter Score: ")
try:
    score = float(score)

except:
    score = -1

if (score >=0) & (score <=1):
    if score >= .9:
        print('A')
    elif score >= .8:
        print('B')
    elif score >= .7:
        print('C')
    elif score >= .6:
        print('D')
    elif score < .6:
        print('F')
else:
    print("Error please enter valid value (numerical value)")
