def writeBio(file, bio):
	keys = list(bio.keys())
	for key in keys:
		if key == "exercises":
			file.write("EXERCISES\n")
			for opt in bio[key]:
				file.write(opt + "\n")
		else:
			file.write(bio[key] + "\n")

def getExercises(level):
	exercises = []
	print("Enter some exercises below. Enter \"exit\" to exit")
	choice = input()
	while choice != "exit":
		exercises.append(choice)
		choice = input()
	#print(exercises)
	return exercises


def getBioInfo(userName):
	bio = {}
	bio["username"] = userName
	bio["pw"] = input("Enter a password: ")
	bio["name"] = input("Enter your name: ")
	bio["age"] = input("Enter your age: ")
	bio["pronouns"] = input("Enter your pronouns: ")
	bio["height"] = input("Enter your height: ")
	bio["weight"] = input("Enter your weight: ")
	bio["level"] = input("Enter low, medium, or high: ")
	bio["exercises"] = getExercises(bio["level"]) # NUMBER EXERCISES?
	return bio

def getFilePath(userName):
	fileName = userName + ".txt"
	filePath = "./userInfo/" + fileName
	return filePath


def createProfile(userName):
	bio = getBioInfo(userName)
	#print(bio)
	file = open(getFilePath(userName), "w+")
	writeBio(file, bio)
	file.close()


def isNameFree(userName):
	fileName = userName + ".txt"
	filePath = "./userInfo/" + fileName
	try:
		file = open(filePath,  "r+")
	except:
		file = open(filePath,  "w+")
	lines = file.readlines()
	#print(lines)
	file.close()
	if lines == []:
		return True
	else:
		return False

def signIn():
	print("signIn")

def signUp(): # don't quit if userName is not available
	#print("signUp")
	userName = input("Please enter your username: ")
	available = isNameFree(userName) # checks if the username is free or not
	#print(available)
	while not available:
		print("The username " + userName + " already exists. Please try another one")
		userName = input("Please enter another username: ")
		available = isNameFree(userName)
	print("That username is available!")
	userInfo = createProfile(userName)



def main():
	print("Hello and welcome to your personalized health dashboard!")
	print("Would you like to sign in or sign up?")
	userChoice = input("Please enter \"in\" or \"up\": ")

	while not (userChoice == "in" or userChoice == "up"):
		userChoice = input("Input error; type \"in\" or \"up\": ")

	if userChoice == "in":
		print("The User wants to sign in")
		signIn()
	else:
		print("The User wants to sign up")
		signUp()

