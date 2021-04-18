from googleapiclient.discovery import build
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def getVideos(interest):
	apiKey = "AIzaSyA1Ge1vSeCOXxqk72rpM4IDVlweHXCS3ws"
	youtube = build('youtube', 'v3', developerKey=apiKey)
	request = youtube.search().list(
		part='snippet',
		maxResults=10,
		q=interest,
		relevanceLanguage="en",
		#order="rating",
		type="video"
	)
	response = request.execute()
	items = response['items']
	urls = []
	videos = []
	images = []
	ids = []
	for item in items:
		video = item['snippet']['title']
		videos.append(video)
		videoId = item['id']['videoId']
		url = 'https://www.youtube.com/watch?v=' + videoId
		urls.append(url)
		image = item['snippet']['thumbnails']['default']['url']
		images.append(image)
		itemId = item['id']['videoId']
		ids.append(itemId)
	return urls, videos, images, ids

def getChannels(interest):
	apiKey = "AIzaSyA1Ge1vSeCOXxqk72rpM4IDVlweHXCS3ws"
	youtube = build('youtube', 'v3', developerKey=apiKey)
	request = youtube.search().list(
		part='snippet',
		maxResults=10,
		q=interest,
		relevanceLanguage="en",
		#order="rating",
		type="channel"
	)
	response = request.execute()
	items = response['items']
	print(items[0])
	urls = []
	names = []
	images = []
	ids = []
	for item in items:
		channelId = item['id']['channelId']
		url = 'https://www.youtube.com/watch?v=' + channelId
		urls.append(url)
		name = item['snippet']['channelTitle']
		names.append(name)
		image = item['snippet']['thumbnails']['default']['url']
		images.append(image)
		itemId = item['id']['channelId']
		ids.append(itemId)
	return urls, names, images, ids


def saveImages(images, ids): # images are image URLs, ids are the unique id of the channel or video
	imgPaths = []
	for spot in range(10):
		response = requests.get(images[spot])
		img = Image.open(BytesIO(response.content))
		#filePath = "./images/" + ids[spot] + ".jpg"
		filePath = getFilePath(ids[spot], ".jpg")
		imgPaths.append(filePath)
		img = img.save(filePath)
	return imgPaths


def writeBio(file, bio):
	keys = list(bio.keys())
	for key in keys:
		if key == "Interests":
			file.write("INTERESTS\n")
			for opt in bio[key]:
				file.write(opt + "\n")
		else:
			file.write(bio[key] + "\n")

def inputInterests():
	interests = []
	print("Enter some interests below. Enter \"exit\" to exit")
	choice = input()
	while choice != "exit":
		interests.append(choice)
		choice = input()
	#print(interests)
	return interests


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
	bio["Interests"] = inputInterests() # NUMBER INTERESTS?
	return bio


def deleteProfile(username):
	bioPath = getFilePath(username, ".txt")
	fitnessPath = getFilePath(username, ".csv")
	os.remove(bioPath)

	doesFitExist = doesNameExist(username, ".csv")
	if doesFitExist:
		os.remove(fitnessPath)

def getFilePath(name, ext):
	fileName = name + ext
	filePath = ""
	if ext == ".txt":
		filePath = "./userInfo/" + fileName
	if ext == ".csv":
		filePath = "./fitnessInfo/" + fileName
	if ext == ".jpg":
		filePath = "./images/" + fileName
	return filePath


def createProfile(username):
	bio = getBioInfo(username)
	#print(bio)
	file = open(getFilePath(username, '.txt'), "w+")
	writeBio(file, bio)
	file.close()


def isNameFree(username, ext):
	filePath = getFilePath(username, ext)
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

def doesNameExist(username, ext):
	filePath = getFilePath(username, ext)
	try:
		file = open(filePath, "r+")
	except:
		return False
	file.close()
	return True

def doesNameExistCSV(username, ext):
	filePath = "./fitnessInfo/" + username + '.csv'
	try:
		file = open(filePath, "r+")
	except:
		return False
	file.close()
	return True


def checkPassword(username, password):
	filePath = getFilePath(username, '.txt')
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
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[2]

def getAge(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[3]

def getPronouns(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[4]

def getHeight(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[5]

def getWeight(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[6]

def getLevel(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	return lines[7]

def getInterests(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	interests = []
	atInterests = False
	for line in lines:
		if atInterests:
			interests.append(line)
		if line == "INTERESTS":
			atInterests = True
	file.close()
	return interests

def signedIn(username):
	print(getName(username) + ", you are now signed in.")


def signIn():
	print("signIn")
	username = input("Please enter your username: ")
	exists = doesNameExist(username, '.txt') # checks if username is in database already
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
	available = isNameFree(username, '.txt') # checks if the username is free
	#print(available)
	while not available:
		print("The username \"" + username + "\" already exists. Please try another one")
		username = input("Please enter another username: ")
		available = isNameFree(username, '.txt')
	print("That username is available!")
	userInfo = createProfile(username)
	choice = input("Would you like to sign in? Enter \"yes\" or \"no\": ")
	if choice == "yes":
		signIn()
	else:
		print("Have a nice day!")


def makeCSVFile(username):
	print('in1')
	path = "./fitnessInfo/" + username + '.csv'
	exists = doesNameExistCSV(username, '.csv')
	if exists:
		print('exists')
		f = open(path, 'r+')
	else:
		print('doesnt')
		data = {"dates": [], "distance (miles)": [], "duration (hh:mm:ss)": [], "pace (mph)": []}
		data_df = pd.DataFrame(data)
		data_df.to_csv(path)
		f = open(path, 'r+')
		print('done')

def getDF(username):
	path = "./fitnessInfo/" + username + '.csv'
	df = pd.read_csv(path, index_col=0)
	return df



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

