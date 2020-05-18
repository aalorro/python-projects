#!/usr/bin/python3

# This python program is to determine the number of words
# in a sentence or paragraph.

print("Let's count the number of words in a sentence or paragraph\n")

string_1 = input("Copy paste a sentence or paragraph here: ")

words = string_1.split()
num = len(words)

print("\n")
print("There are " + str(num) + " words in the sentence.")
print("\n")


