import tkinter as tk
import logic as l
import webbrowser
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import datetime


user_data = {}
main_username = "blank"
user_data["Username"] = "blank"
#user_data["Interests"] = "blank1"
#name = tk.StringVar()

all_stuff = {'bowling': {'urls': ['https://www.youtube.com/watch?v=yGWwBbs8Q4w', 'https://www.youtube.com/watch?v=z6AVRUEqTkQ', 'https://www.youtube.com/watch?v=9d_UYHOqgdA', 'https://www.youtube.com/watch?v=qtR-twJOdUU', 'https://www.youtube.com/watch?v=0S8LcKO0-aw', 'https://www.youtube.com/watch?v=cwHRegcjasg', 'https://www.youtube.com/watch?v=CACAmH4r1fw', 'https://www.youtube.com/watch?v=2-EUNXTWlq0', 'https://www.youtube.com/watch?v=Z9O67Wjrc-8', 'https://www.youtube.com/watch?v=11nlxBHpJSQ'], 'names': ['2021 PBA Chameleon Championship Eliminator Finals (WSOB XII) | Full PBA Bowling Telecast', '2021 NCAA Bowling Championship Final', '2021 Kia PBA Tournament of Champions Stepladder Finals | Full PBA Bowling Telecast', 'Can 4 Guys Beat A Professional Bowler?!', '2021 PBA US Open Stepladder Finals', 'Mookie Betts Rolls Perfect 300 Game in PBA World Series of Bowling', 'Bowling Trick Shots | Dude Perfect', '2021 NCAA bowling championship: Nebraska vs. Arkansas State | FULL REPLAY', 'Bowling | 2021 Indiana High School Bowling Singles Stepladder Finals', '2021 PBA Players Championship Finals'], 'images': ['https://i.ytimg.com/vi/yGWwBbs8Q4w/default.jpg', 'https://i.ytimg.com/vi/z6AVRUEqTkQ/default.jpg', 'https://i.ytimg.com/vi/9d_UYHOqgdA/default.jpg', 'https://i.ytimg.com/vi/qtR-twJOdUU/default.jpg', 'https://i.ytimg.com/vi/0S8LcKO0-aw/default.jpg', 'https://i.ytimg.com/vi/cwHRegcjasg/default.jpg', 'https://i.ytimg.com/vi/CACAmH4r1fw/default.jpg', 'https://i.ytimg.com/vi/2-EUNXTWlq0/default.jpg', 'https://i.ytimg.com/vi/Z9O67Wjrc-8/default.jpg', 'https://i.ytimg.com/vi/11nlxBHpJSQ/default.jpg'], 'ids': ['yGWwBbs8Q4w', 'z6AVRUEqTkQ', '9d_UYHOqgdA', 'qtR-twJOdUU', '0S8LcKO0-aw', 'cwHRegcjasg', 'CACAmH4r1fw', '2-EUNXTWlq0', 'Z9O67Wjrc-8', '11nlxBHpJSQ']}, 'parkour': {'urls': ['https://www.youtube.com/watch?v=cR_ZvX3Hg-w', 'https://www.youtube.com/watch?v=6zkhxeU_WqI', 'https://www.youtube.com/watch?v=aA_ZzKXSbo8', 'https://www.youtube.com/watch?v=sRbvkPqBnTg', 'https://www.youtube.com/watch?v=x75FoBGQxTc', 'https://www.youtube.com/watch?v=zdl3yUaJ25o', 'https://www.youtube.com/watch?v=lw0myT99ro4', 'https://www.youtube.com/watch?v=zmLtl1B7zM4', 'https://www.youtube.com/watch?v=YB1gEz0e3hM', 'https://www.youtube.com/watch?v=Nxb26OAtp9w'], 'names': ['ESCAPING ANGRY TEACHER (Epic Parkour POV Chase)', 'STORROR BEST OF Parkour POV Worldwide 🌎', 'LATE FOR SCHOOL - Parkour POV', 'Paris Rooftop Parkour POV 🇫🇷', 'Late For School Parkour POV (Winter Edition)', 'BEST of STORROR Parkour Water Challenges 🌊', 'ESCAPING ANGRY MOM (Epic Parkour Chase in Paris)', 'CRAZY THIEF VS PARKOUR - POV', 'Late For My Flight - Parkour POV', 'Texas Parkour POV 🇺🇸'], 'images': ['https://i.ytimg.com/vi/cR_ZvX3Hg-w/default.jpg', 'https://i.ytimg.com/vi/6zkhxeU_WqI/default.jpg', 'https://i.ytimg.com/vi/aA_ZzKXSbo8/default.jpg', 'https://i.ytimg.com/vi/sRbvkPqBnTg/default.jpg', 'https://i.ytimg.com/vi/x75FoBGQxTc/default.jpg', 'https://i.ytimg.com/vi/zdl3yUaJ25o/default.jpg', 'https://i.ytimg.com/vi/lw0myT99ro4/default.jpg', 'https://i.ytimg.com/vi/zmLtl1B7zM4/default.jpg', 'https://i.ytimg.com/vi/YB1gEz0e3hM/default.jpg', 'https://i.ytimg.com/vi/Nxb26OAtp9w/default.jpg'], 'ids': ['cR_ZvX3Hg-w', '6zkhxeU_WqI', 'aA_ZzKXSbo8', 'sRbvkPqBnTg', 'x75FoBGQxTc', 'zdl3yUaJ25o', 'lw0myT99ro4', 'zmLtl1B7zM4', 'YB1gEz0e3hM', 'Nxb26OAtp9w']}, 'lifting': {'urls': ['https://www.youtube.com/watch?v=emxEhfwori4', 'https://www.youtube.com/watch?v=_dCtNLMQ07E', 'https://www.youtube.com/watch?v=q9Cux6Ed20g', 'https://www.youtube.com/watch?v=se5tQWjKzdw', 'https://www.youtube.com/watch?v=a2tycd7W0oI', 'https://www.youtube.com/watch?v=S4Mibq6wROA', 'https://www.youtube.com/watch?v=2L7OpEdsuho', 'https://www.youtube.com/watch?v=FtzuPQNwiS0', 'https://www.youtube.com/watch?v=oHyqUJ6YA2I', 'https://www.youtube.com/watch?v=s8hWQwFwayo'], 'names': ['7 Things I Wish I Knew When I Started Lifting', 'Casually Explained: Lifting', '20 Common Lifting Mistakes To Avoid! (Are You Guilty Of These?)', 'Who Can Lift the Most Weight Challenge w/ World&#39;s Strongest Man', 'SOME OF THE BEST LIFTING ADVICE FROM OLYMPIC MEDALIST DMITRY KLOKOV', 'GYM IDIOTS 2020 - Tough Guys, Ego Lifting &amp; More', 'GYM IDIOTS 2020 - Heavy Squats, Ego Lifting &amp; More', 'Professional Powerlifters React to Lifting Scenes in Hollywood', '5 Things I Wish I Knew Before I Started Lifting Weights', 'FOCUS , LISTEN, LIFT - Best Gym Training Motivation'], 'images': ['https://i.ytimg.com/vi/emxEhfwori4/default.jpg', 'https://i.ytimg.com/vi/_dCtNLMQ07E/default.jpg', 'https://i.ytimg.com/vi/q9Cux6Ed20g/default.jpg', 'https://i.ytimg.com/vi/se5tQWjKzdw/default.jpg', 'https://i.ytimg.com/vi/a2tycd7W0oI/default.jpg', 'https://i.ytimg.com/vi/S4Mibq6wROA/default.jpg', 'https://i.ytimg.com/vi/2L7OpEdsuho/default.jpg', 'https://i.ytimg.com/vi/FtzuPQNwiS0/default.jpg', 'https://i.ytimg.com/vi/oHyqUJ6YA2I/default.jpg', 'https://i.ytimg.com/vi/s8hWQwFwayo/default.jpg'], 'ids': ['emxEhfwori4', '_dCtNLMQ07E', 'q9Cux6Ed20g', 'se5tQWjKzdw', 'a2tycd7W0oI', 'S4Mibq6wROA', '2L7OpEdsuho', 'FtzuPQNwiS0', 'oHyqUJ6YA2I', 's8hWQwFwayo']}}

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

		for frame in (FirstPage, SignInPage, SignUpPage0, SignUpPage1, MainPage, LogWorkoutPage, DataVis):
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
		username_exists = l.doesNameExist(username, '.txt')
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

#all_stuff = {}

class MainPage(tk.Frame):
	def __init__(self, master, cont):
		self.cont = cont
		tk.Frame.__init__(self, master)
		self.buttons = [tk.Button(self), tk.Button(self), tk.Button(self), tk.Button(self), tk.Button(self), tk.Button(self)]
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_columnconfigure(3, weight=1)
		self.grid_columnconfigure(4, weight=1)
		self.lab = tk.Label(self, text="Welcome to your Health & Fitness Account!", font='Helvetica 18 bold')
		self.lab.grid( row = 0, column=1, columnspan=3, pady=15)
		
		tk.Button(self, text="Sign Out", command = lambda: cont.display_page(FirstPage)).grid(row=0, column=0)
		tk.Button(self, text="Refresh Page", command=lambda: self.update_page()).grid(row=0, column=4)
		tk.Button(self, text="Log Food").grid(row=1, column=0, pady=20)

		tk.Button(self, text="Log Workout", command=lambda: self.to_logworkout_page()).grid(row=1, column=1, pady=20)

		tk.Button(self, text="View Running Data", command=lambda: self.to_data_vis()).grid(row=2, column=1, columnspan=3, rowspan = 2, pady=10)


	def to_logworkout_page(self):
		l.makeCSVFile(main_username)
		self.cont.display_page(LogWorkoutPage)

	def to_data_vis(self):
		l.makeCSVFile(main_username)
		self.cont.display_page(DataVis)

	def oepn_url(self, url):
		webbrowser.open('nfl.com', new=1)

	def show_video_content(self, interest):
		print(interest)
		local_interest = all_stuff[interest]
		j = 4
		q = 0
		for title, url in zip(local_interest["names"], all_stuff[interest]['urls']):
			print('q: ', q)
			j1 = j + 1
			self.buttons[q].grid(row=j, column=1, pady=10)
			self.buttons[q].config(text= title, command = lambda url = url: self.oepn_url(url))
			#tk.Button(self, text=title, command = lambda url = url: self.oepn_url(url)).grid(row=j, column=1, pady=10)
			j += 1
			q += 1
			if j == 10:
				break


	def update_page(self):
		self.get_all_user_data()
		l1 = user_data["Interests"]
		print(l1)
		for i in range(len(l1) - 1):
			print("i: ", i)
			# plae button on screen
			tk.Button(self, text="Show Videos Related to " + l1[i], command = lambda i=i: self.show_video_content(l1[i])).grid(row=i+4, column=0, pady=20)
			# append to user_videos
			#user_urls, user_videos, user_images, user_ids = 									#THIS IS WHAT I NEED ->: l.getVideos(user_data["Interests"][i])
			#all_stuff[user_data["Interests"][i]] = {"urls": user_urls, "names": user_videos, "images": user_images, "ids": user_ids}

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


		
class LogWorkoutPage(tk.Frame):
	def __init__(self, master, cont):
		
		self.cont = cont
		tk.Frame.__init__(self, master)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		tk.Button(self, text="Back", command = lambda: cont.display_page(MainPage)).grid(row=0, column=0, padx=10, pady=10)

		tk.Label(self, text='Enter data from your latest run!').grid(row=1, column=0, columnspan=2, padx=10, pady=10)

		tk.Label(self, text='Date (MM/DD/YYYY)').grid(row=2, column=0, pady=10)
		self.e1 = tk.Entry(self)
		self.e1.grid(row=2, column=1)

		tk.Label(self, text='Distance Run (miles)').grid(row=3, column=0, pady=10)
		self.e2 = tk.Entry(self)
		self.e2.grid(row=3, column=1)

		tk.Label(self, text='Duration (hours)').grid(row=4, column=0, pady=10)
		self.e3 = tk.Entry(self)
		self.e3.grid(row=4, column=1)

		tk.Button(self, text="Log Run", command=lambda: self.log_run()).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

	def check_user_input(self):
		date = self.e1.get()
		print(date)
		dist = self.e2.get()
		time = self.e3.get()
		month = date[0:2]
		day = date[3:5]
		year = 2021
		#year = date[-4:-1]
		print("month: ", month)
		print("day: ", day)
		print("year: ", year)
		datetime.datetime(int(year), int(month), int(day))
		
		try:
			#month, day, year = date.split('/')
			
			float_dist = float(dist)
			float_time = float(time)
		except:
			print("Please make sure all entries are valid!")
			return False

		return True

	def log_run(self):
		date = self.e1.get()
		dist = round(float(self.e2.get()), 2)
		time = round(float(self.e3.get()), 2)
		if not(self.check_user_input()):
			return None
		path = "./fitnessInfo/" + main_username + '.csv'
		df = l.getDF(main_username)
		print(df.tail())
		pace = round(dist/time, 2)
		if df.empty:
			print('empty')
			da = {'dates': [date]}
			df1 = pd.DataFrame(da)

			data = {'distance (miles)': [dist], "duration (hh:mm:ss)": [time], "pace (mph)": [pace]}
			data_df = pd.DataFrame(data)
			result = pd.concat([df1, data_df], axis = 1)
			result.to_csv(path)
		else:

			df.loc[len(df.index)] = [date, dist, time, pace]
			#df2 = {'dates': date, 'distance (miles)': dist, "duration (hh:mm:ss)": time, "pace (mph)": pace}
			#df = df.append(df2, ignore_index=True)
			df.to_csv(path)


		print(df.tail())
		
		
		print("data written successfully!")
		self.e1.delete(0, tk.END)
		self.e2.delete(0, tk.END)
		self.e3.delete(0, tk.END)


class DataVis(tk.Frame):
	def __init__(self, master, cont):
		self.cont = cont

		

		tk.Frame.__init__(self, master)
		self.subframe = tk.Frame(self, bg='snow', height=180)
		self.subframe.pack(fill=tk.X, side=tk.TOP)
		tk.Button(master=self.subframe, text="Back", command = lambda: cont.display_page(MainPage)).grid(row=0, column=0, padx=10, pady=10)
		tk.Label(master=self.subframe, text='Data From Date (MM/DD/YYYY').grid(row=1, column=0)
		self.e1 = tk.Entry(master=self.subframe)
		self.e1.grid(row=2, column=0)

		tk.Label(master=self.subframe, text='Data To Date (MM/DD/YYYY').grid(row=1, column=1)
		self.e2 = tk.Entry(master=self.subframe)
		self.e2.grid(row=2, column=1)

		

		self.subframe1 = tk.Frame(self)
		self.subframe1.pack(side=tk.BOTTOM)




		self.create_widgets()

		

	def create_widgets(self):
		# the figure that will contain the plot
		fig = Figure(figsize = (8, 5), dpi = 100)
	  
		# adding the subplot
		plot1 = fig.add_subplot(111)
	  
	  
		# creating the Tkinter canvas
		# containing the Matplotlib figure
		canvas = FigureCanvasTkAgg(fig, self.subframe1)  
	  
		# placing the canvas on the Tkinter window
		canvas.get_tk_widget().pack()

		#canvas.show()
	  
		# creating the Matplotlib toolbar
		toolbar = NavigationToolbar2Tk(canvas, self.subframe1)
		toolbar.update()
	  
		# placing the toolbar on the Tkinter window
		canvas.get_tk_widget().pack()

		tk.Button(master=self.subframe, command = lambda: self.plot(canvas, plot1, 'distance (miles)'), text= "Plot Miles Run").grid(row=0, rowspan=2, column=2, padx=10)
		tk.Button(master=self.subframe, command = lambda: self.plot(canvas, plot1, "pace (mph)"), text= "Plot Running Pace").grid(row=0, rowspan=2, column=3, padx=10)
		tk.Button(master=self.subframe, command = lambda: self.plot(canvas, plot1, "duration (hh:mm:ss)"), text= "Plot Time Run").grid(row=0, rowspan=2, column=4, padx=10)


	def plot(self, canvas, plot, val):
		start_date = self.e1.get()
		end_date = self.e2.get()

		df = self.get_clean_data(start_date, end_date)
		print(df)

		#y = [i**2 for i in range(101)]
		plot.clear()

		plot.set(xlabel='Day', ylabel=val)

		plot.plot(df[val], color='green')
		canvas.draw()

	def get_clean_data(self, start_date, end_date):
		df = l.getDF(main_username)
		df['dates'] = pd.to_datetime(df['dates'])
		df = df.set_index(['dates'])
		df1 = df.loc[start_date : end_date]
		return df1



		#tk.Button(self, text = "Main Page", command = lambda: cont.display_page(FirstPage)).grid(row=2, column=1, padx=15, pady=5)


app_instance = HealthGUI()
#app_instance.mainloop()