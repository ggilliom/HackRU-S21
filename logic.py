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


def getBioInfo(username):
	bio = {}
	bio["username"] = username
	bio["pw"] = input("Enter a password: ")
	bio["name"] = input("Enter your name: ")
	bio["age"] = input("Enter your age: ")
	bio["pronouns"] = input("Enter your pronouns: ")
	bio["height"] = input("Enter your height: ")
	bio["weight"] = input("Enter your weight: ")
	bio["level"] = input("Enter low, medium, or high: ")
	bio["exercises"] = getExercises(bio["level"]) # NUMBER EXERCISES?
	return bio

def getFilePath(username):
	fileName = username + ".txt"
	filePath = "./userInfo/" + fileName
	return filePath


def createProfile(username):
	bio = getBioInfo(username)
	#print(bio)
	file = open(getFilePath(username), "w+")
	writeBio(file, bio)
	file.close()


def isNameFree(username):
	filePath = getFilePath(username)
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

def doesNameExist(username):
	filePath = getFilePath(username)
	try:
		file = open(filePath, "r+")
	except:
		return False
	file.close()
	return True


def checkPassword(username, password):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	if lines[1] == password:
		return True
	return False


def getFileLines(file):
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

def getName(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[2]

def getAge(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[3]

def getPronouns(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[4]

def getHeight(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[5]

def getWeight(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[6]

def getLevel(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[7]

def getExercises(username):
	filePath = getFilePath(username)
	file = open(filePath, "r")
	lines = getFileLines(file)
	exercises = []
	atExercises = False
	for line in lines:
		if atExercises:
			exercises.append(line)
		if line == "EXERCISES":
			atExercises = True
	file.close()
	return exercises

def signedIn(username):
	print(getName(username) + ", you are now signed in.")


def signIn():
	print("signIn")
	username = input("Please enter your username: ")
	exists = doesNameExist(username) # checks if username is in database already
	if exists:
		password = input("Please enter your password: ")
		isCorrect = checkPassword(username, password)
		if isCorrect:
			print("Username and password accepted. Welcome, " + getName(username))
			signedIn(username)
		else:
			print("Incorrect password.")

	else:
		print("That username does not exist in our database. Would you like to sign up?")
		choice = input("Enter \"yes\" or \"no\": ")
		if choice == "yes":
			signUp()
		else:
			print("Have a nice day!")



def signUp(): 
	print("signUp")
	username = input("Please enter your username: ")
	available = isNameFree(username) # checks if the username is free
	#print(available)
	while not available:
		print("The username \"" + username + "\" already exists. Please try another one")
		username = input("Please enter another username: ")
		available = isNameFree(username)
	print("That username is available!")
	userInfo = createProfile(username)
	choice = input("Would you like to sign in? Enter \"yes\" or \"no\": ")
	if choice == "yes":
		signIn()
	else:
		print("Have a nice day!")




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

