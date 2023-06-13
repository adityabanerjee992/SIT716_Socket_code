import sqlite3
import hashlib


conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS data (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "hello", hashlib.sha256(
    "hello".encode()).hexdigest()
username2, password2 = "heelo1", hashlib.sha256(
    "hello1".encode()).hexdigest()
username3, password3 = "hello2", hashlib.sha256(
    "hello2".encode()).hexdigest()

cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username1, password1))
cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username2, password2))
cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username3, password3))

conn.commit()
