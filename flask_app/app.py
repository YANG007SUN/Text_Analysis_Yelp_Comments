from flask import render_template, redirect, Flask, jsonify, url_for, jsonify
import data_processer
from flask import request
import sys




app = Flask(__name__)

@app.route("/")
def home():
    # default summary data
    summary_data = {
        "text":"I like orange chicken a lot. Great place to go! Strongly recommended!",
        "polarity":0.21,
        "subjecivity":0.81
    }
    return render_template("index.html", summary = summary_data)

@app.route("/",methods=["POST", "GET"])
def my_review_value():
    text = request.form["review"]
    summary_data = data_processer.text_summary(text)
    return render_template("index.html", summary = summary_data)


if __name__=="__main__":
    app.run(debug=True)










