# join me in death.
import socket, sys
from message_box import ServerTimeOutError, ServerConnectionResetError, ServerConnectionRefusedError
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
		ServerTimeOutError()
		sys.exit()

    # ConnectionResetError
	except ConnectionResetError:
		print("ConnectionResetError")
		ServerConnectionResetError()
		sys.exit()

	# ConnectionRefusedError		
	except ConnectionRefusedError:
		print("ConnectionRefusedError")
		ServerConnectionRefusedError()
		sys.exit()

