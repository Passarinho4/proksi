from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Ja jebe"

@app.route("/xd")
def xd():
    return "trololo"