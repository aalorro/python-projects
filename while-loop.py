#! /usr/bin/python3
# Python program using 'while loop' to calculate sum of integers
print()
print("This python program calculates the sum of all integers between 0 and the number you input")
print()

num = int(input("Enter a positive integer: "))
init_num = num
sum = 0

while  num > 0:
    sum += num
    num -= 1

print(str(init_num) + " is the initial number")
print(str(sum) + " is the sum of all integers between 0 and " + str(init_num))

