print("Good Morning!")

choice =''
a = 0
while choice.upper() != 'Q':
	print("What would you like to do?")
	print("S - Create a new log")
	print("Q - Quit")
	choice = input("What do you want to do?")
	
	if choice == "S":
		a+=1
		x = input("How Many Hours of sleep did you get?")
		print(x)
		print('Good! Now let me add this to your schedule.')
return x/a


print("Have a good day!")