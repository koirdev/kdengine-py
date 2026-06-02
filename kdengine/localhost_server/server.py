# localhost server

import socket, time

print("Loading...")
server = socket.socket()
server.bind(('localhost', 2555))
server.listen(1)
print("Listening new connections...")
conn, addr = server.accept()

print('Connected:', addr)
conn.close()
print("Connection closed")

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
time.sleep(3)
conn.close()
