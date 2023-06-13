import socket
import hashlib
import sqlite3
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1335))
s.listen(10)


def conn_handler(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM data WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login Successfull".encode())
    else:
        c.send("Ops! Login failed!".encode())


while True:
    clientsocket, address = s.accept()
    threading.Thread(target=conn_handler, args=(clientsocket,)).start()

    print(f"Hurray! Connection from {address} has been established!")
    # clientsocket.send(bytes("Welcome to my server!", "utf-8"))
    # clientsocket.close()
