import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 59701))
s.listen(5)

print("Server listening on port 55555")

while True:
    client, address = s.accept()
    print("Connected to", address)
    client.send(bytes("Welcome to the server!", "utf-8"))
    client.close()
