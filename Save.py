names = []
runs = []



def username():
	name = input("Hello! What is your name? ")
	names.append(name)
	
def newRun():
	run = float(input("How many miles did you run? "))
	runs.append(run)
	
	
def runfile():
	sname = str(names)
	srun = str(runs)

	file = open('run.txt','w')
	file.write(sname)
	file.write(srun)
	file.close()
	

def main():
	choice = ''
	while choice.upper() != 'Q':
		print('________________________________________________')
		print("Welcome to RunTracker! These are your options: ")
		print('')
		print("1 - Add a new run!")
		print('')
		print("2 - Show your Run!")
		print('')
		print("3 - Get your day to day average!")
		print('')
		print("Q - Sign Out")
		print('')
		print('')
		choice = input("What would you like to do? ")
		print('')
		print('________________________________________________')
		
		if choice == '1':
			newRun()
		elif choice == '2':
			printRun(user)
		elif choice == '2':
			averageRun(user)
		elif choice == 'Q':
			print("Good Bye!")

username()
main()
runfile()
