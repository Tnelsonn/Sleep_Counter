def login():
	user = input("Enter your name: ")
	print("Hello how are you?, " + user)

	file = open("run.txt", "a+")
	file.close()

	file = open("run.txt", "r")
	lines = file.readlines()

	users = {}
	if len(lines)> 0:
		file.seek(0,0)
		users = eval(file.read())

	file.close()

	if user in users:
		return user
	else:
		users[user] = {}
		file = open("run.txt", "w")
		file.write(str(users))
		file.close()
		return user

def allUsers():
	file = open("run.txt", "r")
	users = eval(file.read())
	file.close()
	return users

def oneUser(username):
	users = allUsers()
	return users[username] 

def saveRun(users):
	file = open("run.txt", "w")
	file.write(str(users))
	file.close()

def newRun(username):
	users = allUsers()
	user = users[username]
	runType = input("What kind of run did you go on?")
	if runType not in user:
		user[runType] = 0
	count = float(input("How many miles did you run?"))
	user[runType] += count
	users[username] = user
	saveRun(users)

def printRun(username):
	user = oneUser(username)
	print()
	for key in user:
		print(f"{key}: {user[key]}")
	print()

def main():
	user = login()
	choice = ''
	while choice.upper() != 'Q':
		print("Welcome to RunTracker! These are your options: ")
		print("1 - Add a new run!")
		print("2 - Show your Run!")
		print("3 - Get your day to day average!")
		print("Q - Sign Out")
		choice = input("What would you like to do?")

		if choice == '1':
			newRun(user)
		elif choice == '2':
			printRun(user)
		elif choice == '2':
			averageRun(user)
		elif choice == 'Q':
			print("Good Bye!")

main()