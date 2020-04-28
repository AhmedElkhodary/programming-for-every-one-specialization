 # a program that repeatedly prompts a user for
 # integer numbers until the user enters 'done'.
 # Once 'done' is entered, print out the largest and smallest of the numbers.

largest = None
smallest = None
while True:
    nums = input("Enter a number: ")



    try:
        if nums == "done":
            break

        num = int(nums)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
