import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 🔴 Hardcoded secret (SonarQube will flag this)
SECRET_KEY = "supersecret123"

@app.route("/cmd")
def run_command():
    # 🔴 Command injection vulnerability
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # 🔴 SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = cursor.execute(query).fetchall()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
