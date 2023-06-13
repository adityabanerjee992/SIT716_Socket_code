import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1335))


msg = s.recv(1024).decode()
s.send(input(msg).encode())
msg = s.recv(1024).decode()
s.send(input(msg).encode())

print(s.recv(1024).decode())

# while True:
#     m = s.recv(20)
#     if len(m) <= 0:
#         break
#     msg = msg + m.decode("utf-8")

# print(msg)
