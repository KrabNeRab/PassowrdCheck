import socket
import re

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 5050))
sock.listen(0)
conn, addr = sock.accept()

pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z!@#$%^&*_+=-]{4,}$')

correct = 'correct password'
uncorrect_password = 'uncorrect password'
while True:
    password = conn.recv(1024).decode()
    if bool(pattern_password.match(password)) == True:
        conn.send(correct.encode())
        break
    else:
        conn.send(uncorrect_password.encode())
conn.close()
