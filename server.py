from flask import Flask, request
import subprocess

import utils

app = Flask(__name__)

@app.route("/")
def hello():
    return utils.hello()

app.debug=True
