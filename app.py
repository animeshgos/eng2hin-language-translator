from flask import Flask, request, render_template

import requests

from translation import translator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():
    output = ""
    input = ""
    if request.method == "POST":
        rawtext = request.form["rawtext"]
        output, input = translator(rawtext)
    return render_template("answer.html", output=output, input=input)


if __name__ == "__main__":
    app.run(debug=True)
