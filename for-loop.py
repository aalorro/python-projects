# Python program that counts the number of characters in a given string

print("This python program counts the number of characters in a string")
print()

string = input("Enter a string: ")
count = 0
for letter in string:
    count += 1

print("You typed: " + string)
print("The number of characters in the string is " + str(count))
