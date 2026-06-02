import pygame
import sys
from config import WARNING_MESSAGE
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton

# ---- Outdated shit ---- (depending).
if WARNING_MESSAGE == 1:
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Warning)
	msg.setText("This build is unstable!")
	msg.setWindowTitle("Warning! - WARNING_MESSAGE")
	msg.show()
	app.exec()

# ---- Window resolution message ----
def WindowModeError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Window mode is wrong!")
	msg.setWindowTitle("Critical Error - WindowModeError")
	msg.show()
	running = False
	pygame.quit()
	app.exec()

# ---- Server messages ----
def ServerTimeOutError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("The connection to the server has timed out or the server is currently unavailable. Please check your internet connection.")
	msg.setWindowTitle("Critical Error - TimeOutError")
	msg.show()
	app.exec()

def ServerConnectionResetError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Connection to the server was interrupted.")
	msg.setWindowTitle("Critical Error - ConnectionResetError")
	msg.show()
	app.exec()

def ServerConnectionRefusedError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("No connection could be made because the target machine actively refused it.")
	msg.setWindowTitle("Critical Error - ConnectionRefusedError")
	msg.show()
	app.exec()

# ---- Other messages ----
def LevelNotFounded():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Level not founded.")
	msg.setWindowTitle("Critical Error - LevelNotFounded")
	msg.show()
	ErrorLog()
	running = False
	app.exec()

def MainCoreInitError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Game initialization failed.")
	msg.setWindowTitle("Critical Error - MainCoreInitError")
	msg.show()
	MainCoreInitErrorLog()
	app.exec()	
	
def FileCorruptionErrorMSG():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("File corruption error.")
	msg.setWindowTitle("Critical Error - FileCorruptionError")
	msg.show()
	InitErrorLog()
	app.exec()

# ---- URL message stuff ----
def URLRequestExceptionError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("A Connection error occurred.")
	msg.setWindowTitle("Critical Error - requests.RequestException")
	msg.show()
	app.exec()

def URLConnectionError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("There was an ambiguous exception that occurred while handling your request.")
	msg.setWindowTitle("Critical Error - requests.ConnectionError")
	msg.show()
	app.exec()

def URLHTTPError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("An HTTP error occurred.")
	msg.setWindowTitle("Critical Error - requests.HTTPError")
	msg.show()
	app.exec()

def URLTooManyRedirectsError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Too many redirects.")
	msg.setWindowTitle("Critical Error - requests.TooManyRedirects")
	msg.show()
	app.exec()

def URLConnectTimeoutError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("The request timed out while trying to connect to the remote server.")
	msg.setWindowTitle("Critical Error - requests.ConnectTimeout")
	msg.show()
	app.exec()

def URLReadTimeoutError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("The server did not send any data in the allotted amount of time.")
	msg.setWindowTitle("Critical Error - requests.ReadTimeout")
	msg.show()
	app.exec()

def URLTimeoutError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("The request timed out.")
	msg.setWindowTitle("Critical Error - requests.Timeout")
	msg.show()
	app.exec()

def URLJSONDecodeError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Couldn’t decode the text into json.")
	msg.setWindowTitle("Critical Error - requests.JSONDecodeError")
	msg.show()
	app.exec()

# ---- ZIP message stuff ----
def ZIPBadFileZipFileError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Bad ZIP file.")
	msg.setWindowTitle("Critical Error - zipfile.BadZipFile")
	msg.show()
	app.exec()

def ZIPLargeZipFileError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Large ZIP file.")
	msg.setWindowTitle("Critical Error - zipfile.LargeZipFile")
	msg.show()
	app.exec()