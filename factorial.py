#!/usr/bin/python

# This python program executes the factorial of a given number
print("This python program calculates the factorial of a user input\n")

num_1 = int(input("Enter a positive integer to get its factorial: "))

init_num = num_1
num_2 = 1

while num_1 > 0:
    num_2 *= num_1
    num_1 -= 1

print("The factorial of " + str(init_num) + " is " + str(num_2))


