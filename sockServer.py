import socket

# Create a Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind To a Host(IP address) and a Port
host = '127.0.0.1'
port = 9999
s.bind((host, port))
# Listen
s.listen(1)
print("Waiting for connection...")
# Implement Loop
while True:
    c, addr = s.accept()
    print(f"Connected successfully to {addr}")
    txt = c.recv(1024)
    print(txt.decode('utf-8'))
    payload = input("Say Something to the client: ")
    c.send(payload.encode('utf-8'))
# Accept, recall that it returns a tuple so its c, addr = s.accept() - This is tuple unpacking
