# Create a program that asks the user to enter their name and age.
# Print out a message that tells them the year that they will turn 100 years old.

# input(): to get user input; output will be a string

name = input("What is your name: ")

currentAge = int(input("What is your age: "))

year100 = 100 - currentAge + 2019

print(name + ", the year that you will turn 100 is " + str(year100))

