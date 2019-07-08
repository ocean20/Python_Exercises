# Ask the user for a number
# Depending on whether the number is odd or even, print out the message to the user

num = int(input("Enter a number: "))

if num % 4 == 0:
	print(str(num) + " is divisible by 4")
elif num % 2 == 0:
	print(str(num) + " is even")
else:
	print(str(num) + " is odd")


# Output:
# 20 is divisible by 4
# 10 is even
# 5 is odd