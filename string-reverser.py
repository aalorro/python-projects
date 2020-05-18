#!/usr/bin/python3

# This python program reverses the inputted string.
print("")
print("This python program will reverse any word or sentence.\n")

string1 = input("Please enter a word or sentence: ")

string2 = ""

for letters in range(len(string1) - 1, -1, -1):
    string2 += string1[letters]

print("The reverse of the string is: " + string2)