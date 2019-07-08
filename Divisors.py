# ask user for a number and then prints a list of the divisors of that number

# range() function: creates a list of numbers from the first number up to last number specified
# x = range(2, 11) 
# [2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Enter a number: "))

div = range(1, num + 1)

listDiv = []

for i in div:
	if num % i == 0:
		listDiv.append(i)

print(listDiv)