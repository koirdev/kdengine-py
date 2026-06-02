from config import ENABLE_DISCORD, DEBUG_MODE
from os_info import PLATFORM_SYS
import pymem

pm = pymem.Pymem()

#If OS/Platform is Windows (ONLY for Windows).
if PLATFORM_SYS == "Windows": 
	ProcessName = "Discord.exe"
else:
	pass

try:
	pm.open_process_from_name(ProcessName) # Searching for 'Discord.exe' process.
	if ENABLE_DISCORD == 1:
		from pypresence import Presence # The simple rich presence client in pypresence
		client_id = "1459514805340868782" # Client ID
		#print(client_id)

		def discordClient():
			try:
				global RPC
				RPC = Presence(client_id) # Initialize the Presence client
				print("Connecting to Discord...")
				RPC.connect() # Start the handshake loop
				print("Connected to Discord")
				RPC.update(state="in development", details="A fork of Shirraria", name="ForkMania") # App description.
			
			except Exception: # If happends any error about Discord connection.
				print("ERROR: Unable to connect to Discord.")
				ENABLE_DISCORD = 0 # Returns '0' just in case.
				print(f"'ENABLE_DISCORD' changed to:", ENABLE_DISCORD)

		def discordClientClose(): # Closes the RPC connection with Discord client.
			RPC.close()
			print("Discord client closed.")

except pymem.exception.ProcessNotFound: #If process 'Discord.exe' was not found (For Windows).
	if DEBUG_MODE == 1:
		print(f"The {ProcessName} process was not found.")
		ENABLE_DISCORD = 0
		print(f"'ENABLE_DISCORD' changed to:", ENABLE_DISCORD)
	else:
		pass

