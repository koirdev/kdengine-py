import os, sys
from urlDownloadContent import *
from config import ASSETS_DIR, SCREENSHOTS_DIR
from os_info import PLATFORM_SYS
from pathlib import Path

#assets_dir_path = "assets" # Path for 'assets' directory.
#screenshots_dir_path = "screenshots" # Path for 'screenshots' directory.
#global assets_exists - Unused.

def checkFiles():
	fileName = (Path(__file__).name)
	if os.path.isdir(ASSETS_DIR): # if 'assets' folder exists. (True)
		#assets_exists = True
		print(f"'{fileName}' - '{ASSETS_DIR}' directory exists.")

	if not os.path.isdir(ASSETS_DIR): # if 'assets' folder not exists. (False)
		print(f"'{fileName}' - '{ASSETS_DIR}' directory is not exists.") 
		downloadAssetsFromURL() # Downloading from URL address a resources for the game.

# Checking OS info for different paths
if PLATFORM_SYS == "Windows":
	SCREENSHOTS_DIR = "screenshots"

if PLATFORM_SYS == "Linux":
	SCREENSHOTS_DIR = "../screenshots"

def checkScreenshotsFolder():
		if os.path.isdir(SCREENSHOTS_DIR): # if 'screenshots' folder exists. (True)
			#assets_exists = True
			print(f"'{SCREENSHOTS_DIR}' directory exists.")

		if not os.path.isdir(SCREENSHOTS_DIR): # if 'screenshots' folder not exists. (False)
			print(f"'{SCREENSHOTS_DIR}' directory is not exists.")
			print(f"Creating new directory named: '{SCREENSHOTS_DIR}'")
			print(f"Creating '{SCREENSHOTS_DIR}' folder for '{PLATFORM_SYS}' system...")
			os.makedirs(SCREENSHOTS_DIR) # Creating a new folder named 'screenshots'


		print("Done.")

checkFiles()

def checkAllFiles():
	pass