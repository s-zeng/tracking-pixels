#! /usr/bin/env python

from flask import Flask, send_file, request
from flask.wrappers import Response
import datetime

app = Flask(__name__)

names_file = "seen.txt"
pixel = "1x1.png"


@app.route("/pixel/<path:name>", methods=["GET"])
def track(name: str) -> Response:
    name = name.split(".")[0]
    with open(names_file, "a") as f:
        f.write(f"{name} from {request.remote_addr}: {datetime.datetime.now()}\n")
    return send_file(pixel, mimetype="image/png")


@app.route("/seen")
def hello() -> Response:
    return send_file(names_file, mimetype="text/plain")


def run():
    app.run(host="0.0.0.0", port=5227)


if __name__ == "__main__":
    run()
