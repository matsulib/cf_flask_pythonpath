from flask import Flask

import utils

app = Flask(__name__)

@app.route("/")
def hello():
    return utils.hello()

app.debug=True
