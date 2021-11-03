import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to a socket
host = '127.0.0.1'
port = 9999
client.connect((host, port))

data = input("Say something to the server: ")
# send and receive messages
while True:
    client.send(data.encode('utf-8'))
    payload = client.recv(1024)
    print(payload.decode('utf-8'))