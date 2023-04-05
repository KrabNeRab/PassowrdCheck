import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(1)
sock.connect(('localhost', 5050))


password = ""
data = ""
while True:
    password = input("Input password: ")
    sock.send(password.encode())
    data = sock.recv(1024).decode()
    print(data)
    if data == 'correct password':
        break

sock.close()

