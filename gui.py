import tkinter as tk
import logic as l
import webbrowser


user_data = {}
main_username = "blank"
user_data["Username"] = "blank"
#user_data["Interests"] = "blank1"
#name = tk.StringVar()

class HealthGUI(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		cont = tk.Frame(self)
		global name
		name = tk.StringVar()
		self.geometry("1200x800")
		self.configure(bg = "cyan")

		storage = tk.Frame(self)
		storage.pack(side = "top", fill = "both", expand = True)

		storage.grid_rowconfigure(0, weight = 1)
		storage.grid_columnconfigure(0, weight = 1)
		#storage.grid_rowconfigure(1, weight = 1)
		#storage.grid_columnconfigure(1, weight = 1)


		# all frames
		self.all_frames = {}

		for frame in (FirstPage, SignInPage, SignUpPage0, SignUpPage1, MainPage):
			f = frame(storage, self)
			self.all_frames[frame] = f
			if frame == MainPage:
				f.configure(bg="sky blue")
			else:

				f.configure(bg="sky blue")
			#f.grid_columnconfigure(0, weight = 1)
			f.grid(row = 0, column = 0, sticky = "nsew")


		self.display_page(FirstPage)
		self.mainloop()

	def display_page(self, f):
		page = self.all_frames[f]
		page.tkraise()

class FirstPage(tk.Frame):
	def __init__(self, master, cont):
		tk.Frame.__init__(self, master)
		
		#self.configure(height=800)
		#self.configure(width=600)
		self.grid_columnconfigure(0, weight=1)
		tk.Label(self, text = "Welcome to BGFit!", font=("Arial", 25), fg="salmon").grid(row=0, column=0, pady=100)
		tk.Button(self, text = "Sign In", command = lambda: cont.display_page(SignInPage)).grid(row=1, column=0, pady=50)	#place(height = 50, width = 100, relx=.5, rely=.5, anchor='center')
		tk.Button(self, text = "Sign Up", command = lambda: cont.display_page(SignUpPage0)).grid(row=2, column=0, pady=50)		#place(height = 50, width = 100, relx=.5, rely=.6, anchor='center')

here = ("Arial", 18)
color = "black"

class SignInPage(tk.Frame):
	def __init__(self, master, cont):
		self.cont = cont
		tk.Frame.__init__(self, master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		tk.Label(self, text = "User Name",font=here,fg=color ).grid(row=0, column=0, pady=10)
		self.e1 = tk.Entry(self)
		self.e1.grid(row=0, column=1)
	

		tk.Label(self, text = "Password",font=here,fg=color ).grid(row=1, column=0, pady=10)
		self.e2 = tk.Entry(self)
		self.e2.grid(row=1, column=1)


		self.sign_in_button = tk.Button(self, text="Sign in", command = lambda: self.try_sign_in())
		self.sign_in_button.grid(row=2, column=0)

		self.back_button = tk.Button(self, text="Return to main menu", command= lambda: cont.display_page(FirstPage))
		self.back_button.grid(row=3, column=0, pady=55)

	def try_sign_in(self):
		global main_username
		username = self.e1.get()
		username_exists = l.doesNameExist(username)
		password = self.e2.get()
		if username_exists:
			is_correct = l.checkPassword(username, password)
			if is_correct:
				main_username = username
				name.set(username)
				self.cont.display_page(MainPage)
			else:
				tk.Label(self, text="Incorrect Password!",bg ="sky blue", font=("Arial", 14), fg="red").grid(row=2, column = 1)


		else:
			tk.Label(self, text="Username does not exist in our data base",bg ="sky blue", font=("Arial", 14), fg="red").grid(row=2, column = 1)




class SignUpPage0(tk.Frame):
	def __init__(self, master, cont):
		self.cont = cont
		tk.Frame.__init__(self, master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		tk.Label(self, text = "Profile User Name",font=here,fg=color ).grid(row=0, column=0, pady=10)
		self.e1 = tk.Entry(self)
		self.e1.grid(row=0, column=1)
	

		tk.Label(self, text = "Password",font=here,fg=color ).grid(row=1, column=0, pady=10)
		self.e2 = tk.Entry(self)
		self.e2.grid(row=1, column=1)

		self.check_username_button = tk.Button(self, text = "Create Account", command=lambda: self.is_username_valid())
		self.check_username_button.grid(row=2, column=0)

	def is_username_valid(self):
		username = self.e1.get()
		password = self.e2.get()
		free = l.isNameFree(username)
		if not(free):
			tk.Label(self, text="That Username is taken! Please try another one",bg ="sky blue", font=("Arial", 14), fg="red").grid(row=2, column = 1)
			print("Usernmae not free")
		else:
			print("free")
			user_data["Username"] = username
			user_data["Password"] = password
			self.cont.display_page(SignUpPage1)
		



class SignUpPage1(tk.Frame):
	def __init__(self, master, cont):
		self.cont = cont
		tk.Frame.__init__(self, master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		

		tk.Label(self, text = "Full Name: ",font=here,fg=color).grid(row=2, column=0, pady=10)
		self.e3 = tk.Entry(self)
		self.e3.grid(row=2, column=1)


		tk.Label(self, text = "Age: ",font=here,fg=color ).grid(row=3, column=0, pady=10)
		self.e4 = tk.Entry(self)
		self.e4.grid(row=3, column=1)


		tk.Label(self, text = "Pronouns: ",font=here,fg=color ).grid(row=4, column=0, pady=10)
		self.e5 = tk.Entry(self)
		self.e5.grid(row=4, column=1)


		tk.Label(self, text = "Height: ",font=here,fg=color ).grid(row=5, column=0, pady=10)
		self.e6 = tk.Entry(self)
		self.e6.grid(row=5, column=1)

		tk.Label(self, text="Weight: ",font=here,fg=color).grid(row=6, column=0, pady=10)
		self.e7 = tk.Entry(self)
		self.e7.grid(row=6, column=1)


		tk.Label(self, text = "Activity Level: ",font=here,fg=color ).grid(row=7, column=0, pady=10)
		self.e8 = tk.Entry(self)
		self.e8.grid(row=7, column=1)

		tk.Label(self, text="Enter 2 - 5 of your health and fitness interests: ").grid(row=8, column=0)
		self.interests = tk.Text(self)
		self.interests.grid(row=8, column=1, rowspan=4)


		self.b = tk.Button(self, text = "Continue", command = lambda: self.get_data([self.e3, self.e4, self.e5, self.e6, self.e7, self.e8]))
		self.b.grid(row=9, column=0, pady=50)

	def parse_interests(self, interest_string):
		return interest_string.split("\n")


	def get_data(self, entries):
		global user_data

		fields = ["Name", "Age", "Pronouns", "Height", "Weight", "Activity Level"]


		for i in range(len(entries)):
			text = entries[i].get()
			user_data[fields[i]] = text
			print(text)

		user_data["Interests"] = self.parse_interests(self.interests.get("1.0", tk.END))
		print(user_data)

		username = user_data["Username"]

		file = open(l.getFilePath(username), "w+")

		l.writeBio(file, user_data)
		self.cont.display_page(FirstPage)

# to store all of the stuff about the videos we are scraping
user_videos = []
user_urls = []
user_images = []
user_ids = []

all_stuff = {}

class MainPage(tk.Frame):
	def __init__(self, master, cont):
		tk.Frame.__init__(self, master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_columnconfigure(3, weight=1)
		self.grid_columnconfigure(4, weight=1)
		self.lab = tk.Label(self, text="Welcome to your Health & Fitness Account!", font='Helvetica 18 bold')
		self.lab.grid( row = 0, column=0, columnspan=3, pady=15)
		
		
		tk.Button(self, text="Refresh Page", command=lambda: self.update_page()).grid(row=0, column=2)
		tk.Button(self, text="Log Food").grid(row=1, column=0, pady=20)
		tk.Button(self, text="Log Workout").grid(row=1, column=1, pady=20)

	def oepn_url(self, url):
		webbrowser.open(url, new=1)

	def show_video_content(self, interest):
		print(interest)
		local_interest = all_stuff[interest]
		j = 2
		for title, url in zip(local_interest["names"], all_stuff[interest]['urls']):
			j1 = j + 1
			#tk.Label(self, text=title).grid(row=j, column=1, pady=10)
			tk.Button(self, text=title, command = lambda url = url: self.oepn_url(url)).grid(row=j, column=1, pady=10)
			j += 1
			if j == 12:
				break


	def update_page(self):
		self.get_all_user_data()
		l1 = user_data["Interests"]
		print(l1)
		for i in range(len(l1) - 1):
			print("i: ", i)
			# plae button on screen
			tk.Button(self, text="Show Videos Related to " + l1[i], command = lambda i=i: self.show_video_content(l1[i])).grid(row=i+2, column=0, pady=20)
			# append to user_videos
			user_urls, user_videos, user_images, user_ids = l.getVideos(user_data["Interests"][i])
			all_stuff[user_data["Interests"][i]] = {"urls": user_urls, "names": user_videos, "images": user_images, "ids": user_ids}

		#print(all_stuff)

		self.lab.config(text = "Welcome to your Health & Fitness Account, " + user_data["Name"])
		
	def get_all_user_data(self):
		global main_username
		global user_data
		print(main_username)
		fields = ["Name", "Age", "Pronouns", "Height", "Weight", "Activity Level"]
		name = l.getName(main_username)
		age = l.getAge(main_username)
		pronouns = l.getPronouns(main_username)
		height = l.getHeight(main_username)
		weight = l.getWeight(main_username)
		act_level = l.getLevel(main_username)
		interests = l.getInterests(main_username)
		data = [name, age, pronouns, height, weight, act_level, interests]
		user_data["Username"] = main_username
		user_data["Interests"] = interests

		for i in range(len(fields)):
			text = data[i]
			user_data[fields[i]] = text

		print(user_data)


		






		#tk.Button(self, text = "Main Page", command = lambda: cont.display_page(FirstPage)).grid(row=2, column=1, padx=15, pady=5)


app_instance = HealthGUI()
#app_instance.mainloop()