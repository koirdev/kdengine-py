# join me in death.
import socket, sys
from message_box import *
from config import IP, PORT, DEBUG_MODE

def RunClient():
	global IP, PORT
	try:
		if DEBUG_MODE == 1:
			print(f"Connecting to:", f"IP:",IP, f"PORT:",PORT)
		client = socket.socket()
		client.connect((IP, PORT))
		if DEBUG_MODE == 1:
			print("Connected.")


		data = client.recv(1024)
		client.close()
		print(data)

    # ---- Excepts ----

    # TimeoutError
	except TimeoutError:
		print("TimeOutError")
		ErrorWinTitle = "TimeOutError"
		ErrorWinText = "The connection to the server has timed out or the server is currently unavailable. Please check your internet connection."
		ErrorWinIcon = "critical"
		ErrorWin()
		sys.exit()

    # ConnectionResetError
	except ConnectionResetError:
		print("ConnectionResetError")
		ErrorWinTitle = "ConnectionResetError"
		ErrorWinText = "Connection to the server was interrupted."
		ErrorWinIcon = "critical"
		ErrorWin()
		sys.exit()

	# ConnectionRefusedError		
	except ConnectionRefusedError:
		print("ConnectionRefusedError")
		ErrorWinTitle = "ConnectionRefusedError"
		ErrorWinText = "No connection could be made because the target machine actively refused it."
		ErrorWinIcon = "critical"
		ErrorWin()
		sys.exit()

