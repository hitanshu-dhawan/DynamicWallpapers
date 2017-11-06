import os
import random
import time

current_dir = os.path.dirname(os.path.realpath(__file__))

# Changes the desktop background
def change_background(current_time_of_day, image_name):
	image_path = current_dir + "/wallpapers/" + current_time_of_day + "/" + image_name
	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri '" + "file://" + image_path + "'")

# Returns the time of as a string ("morning", "afternoon", etc)
def get_time_of_day():
	current_hour = time.localtime().tm_hour
	if (current_hour >= 5 and current_hour <= 7):
		return "sunrise"
	elif (current_hour >= 8 and current_hour <= 11):
		return "morning"
	elif (current_hour >= 12 and current_hour <= 16):
		return "afternoon"
	elif (current_hour >= 17 and current_hour <= 19):
		return "sunset"
	elif (current_hour >= 20 or current_hour <= 4):
		return "night"

# Main loop
while (True):
	# Create a list of images for the current time of day
	file_names = []
	current_time_of_day = get_time_of_day()
	for path, dirs, files in os.walk(current_dir + "/wallpapers/" + current_time_of_day):
		for file in files:
			file_names.append(file)

	# Choose a random wallpaper for the current time of day every 30 minutes
	image_name = random.choice(file_names)
	change_background(current_time_of_day, image_name)
	time.sleep(30*60)