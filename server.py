from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/time")
def time():
    time = datetime.now().__str__()
    return (time + " DIS IS YOUR TIME BITCH")


if __name__ == "__main__":
    app.run()
