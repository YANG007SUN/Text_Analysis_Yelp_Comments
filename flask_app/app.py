from flask import render_template, redirect, Flask, jsonify, url_for, jsonify
import data_processer
from flask import request
import sys


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def my_review_value():
    text = request.form["review"]
    summary_data = data_processer.text_summary(text)
    return render_template("index.html", summary = summary_data)


if __name__=="__main__":
    app.run(debug=True)










