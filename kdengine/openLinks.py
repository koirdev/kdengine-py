import os, sys, webbrowser
from PIL import Image
from config import SCREENSHOTS_DIR, SCREENSHOTS_FILE_PATH, LOG_FILE_NAME
from pathlib import Path
from os_info import PLATFORM_SYS

githubURL = 'https://github.com/koirdev/kdengine-py/'
KD_URL = 'koirdevs_site_is_closed'


if PLATFORM_SYS == "Windows":
	LOG_FILE_NAME = "KD_Engine.log"
else:
	if PLATFORM_SYS == "Linux":
		LOG_FILE_NAME = "../KD_Engine.log"

def OpenLogFile():
	try:
		print(f"Opening '{LOG_FILE_NAME}' file...")
		if PLATFORM_SYS == "Windows":
			os.startfile(LOG_FILE_NAME)
		else:
			if PLATFORM_SYS == "Linux":
				os.system("../" + LOG_FILE_NAME)
		print(f"Log file path: {LOG_FILE_NAME}")

	except FileNotFoundError: # If 'KD_Engine.log' was not found.
		print(f"'{fileName}' - The '{LOG_FILE_NAME}' file was not found or not exist.")
		pass

def OpenGitHubLink():
	fileName = (Path(__file__).name)
	print(f"'{fileName}' - Opening {githubURL} URL address...")
	webbrowser.open(githubURL, new=0)

def OpenkSiteLink():
	fileName = (Path(__file__).name)
	print(f"'{fileName}' - Opening {KD_URL} URL address...")
	webbrowser.open(KD_URL, new=0)

def openScreenshotFile():
	fileName = (Path(__file__).name)
	if PLATFORM_SYS == "Windows":
		screenshot_img = Image.open(SCREENSHOTS_FILE_PATH)		
	if PLATFORM_SYS == "Linux":
		screenshot_img = Image.open("../" + SCREENSHOTS_FILE_PATH)
	print(f"Opening {SCREENSHOTS_FILE_PATH} file...")
	screenshot_img.show()
