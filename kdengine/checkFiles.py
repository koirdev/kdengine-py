import os, sys
from urlDownloadContent import *
from config import *

#assets_dir_path = "assets" # Path for 'assets' directory.
#screenshots_dir_path = "screenshots" # Path for 'screenshots' directory.
#global assets_exists - Unused.

if os.path.isdir(ASSETS_DIR): # if 'assets' folder exists. (True)
	#assets_exists = True
	print(f"{ASSETS_DIR} directory exists.")

if not os.path.isdir(ASSETS_DIR): # if 'assets' folder not exists. (False)
	print(f"{ASSETS_DIR} directory is not exists.") 
	downloadAssetsFromURL() # Downloading from URL address a resources for the game.


def checkScreenshotsFolder():
	if os.path.isdir(SCREENSHOTS_DIR): # if 'screenshots' folder exists. (True)
		#assets_exists = True
		print(f"{SCREENSHOTS_DIR} directory exists.")

	if not os.path.isdir(SCREENSHOTS_DIR): # if 'screenshots' folder not exists. (False)
		print(f"{SCREENSHOTS_DIR} directory is not exists.")
		print(f"Creating new directory named: {SCREENSHOTS_DIR}")
		os.makedirs(SCREENSHOTS_DIR) # Creating a new folder named 'screenshots'
		print("Done.")


def checkAllFiles():
	pass