from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)
@app.route('/')
def index():
    return '<h2>Go to <a href="/htop">/htop</a></h2>'
@app.route('/htop')
def htop():
    name = "Abhay Singh Parihar"
    import getpass
    username = getpass.getuser()

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    # Get top output
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode('utf-8')
    except Exception as e:
        top_output = f"Error getting top output: {e}"

    html = f"""
    <h1>System Monitor</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

