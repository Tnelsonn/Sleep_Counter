print("Good Morning!")

choice =''

while choice.upper() != 'Q':
	print("What would you like to do?")
	print("S - Create a new log")
	print("Q - Quit")
	choice = input("What do you want to do?")
	
	if choice == "S":
		x = input("How Many Hours of sleep did you get?")
		print(x)
		print('Good!')

def slpavg(sleep[],days):

print("Have a good day!")