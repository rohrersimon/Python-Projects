def __init__(self):
    self.numbers = [3, 343, 2, 87, 4.56, 867, 309, 667, 1494, 84, 9544, 53, 2223]

def print_even(number):
	if number % 2 == 0:
		print("Number " + str(number) + " is an even number")
	else:
		print(f"Number " + str(number) + " is an odd number")

numberList = [2, 4, 33454, 445, 5985, 354]

for number in numberList:
	print_even(number)