import os
import random
import sys

from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello_world():
    recipient = os.getenv("RECIPIENT", "world")

    return jsonify({"message": "Hello", "recipient": recipient})

@app.route('/<name>')
def hello_recipient(name):

    if random.randint(1,6) == 6:    # commented to simulated build failure
        raise Exception("Internal error accourred")

    return jsonify({"message": f"Welcome {name}"})

if __name__ == "__main__":
    app.run()