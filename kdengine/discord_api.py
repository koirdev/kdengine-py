from pypresence import Presence # The simple rich presence client in pypresence
import time

client_id = "1459514805340868782" # Game ID
rpc = None

try:
	rpc = Presence(client_id) # Initialize the Presence client

	rpc.connect()
	print("connected") # Start the handshake loop)
	rpc.update(state="in development", details="A fork of Shirraria", name="kdEngine-py (kd_fix-03)") # App description.
			
	while True:
		time.sleep(15)
		print("time upd")
except KeyboardInterrupt:
	print("\nstop")

finally:
	if rpc is not None:
		rpc.close()
		print("stop conn")
