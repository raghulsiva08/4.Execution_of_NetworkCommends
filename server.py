import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8000

server.bind((host, port))
server.listen(5)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Command received:", data)

    result = os.popen(data).read()

    if result == "":
        result = "Command executed but no output"

    conn.send(result.encode())

conn.close()
server.close()