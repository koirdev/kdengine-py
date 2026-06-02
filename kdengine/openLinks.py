import os, sys, webbrowser
from PIL import Image
from config import SCREENSHOTS_DIR, SCREENSHOTS_FILE_PATH, LOG_FILE_NAME

githubURL = 'https://github.com/koirdev/Shirraria'
KD_URL = 'https://koirdev.su/'

def OpenLogFile():
	try:
		print(f"Opening {LOG_FILE_NAME} file...")
		os.startfile(LOG_FILE_NAME)

	except FileNotFoundError: # If 'KD_Engine.log' was not found.
		print(f"The {LOG_FILE_NAME} file was not found or not exist.")
		pass

def OpenGitHubLink():
	print(f"Opening {githubURL} URL address...")
	webbrowser.open(githubURL, new=0)

def OpenkSiteLink():
	print(f"Opening {KD_URL} URL address...")
	webbrowser.open(KD_URL, new=0)

def openScreenshotFile():
	screenshot_img = Image.open(SCREENSHOTS_FILE_PATH)
	print(f"Opening {SCREENSHOTS_FILE_PATH} file...")
	screenshot_img.show()


	