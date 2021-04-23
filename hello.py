# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:59:40 2021

@author: zhaop
"""


"""
from flask import Flask
app = Flask(__name__)
@app.route()
def hello() -> str:
 return "This is Nancy and Sean's website"
app.run()
"""

from flask import Flask, render_template      

app = Flask(__name__)


@app.route("/")
def template():
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Sushi")
def Sushi():
    return render_template("Sushi.html")

@app.route("/Hamburger")
def Hamburger():
    return render_template("Hamburger.html")

@app.route("/HotDog")
def HotDog():
    return render_template("HotDog.html")

@app.route("/Fries")
def Fries():
    return render_template("Fries.html")

@app.route("/Pizza")
def Pizza():
    return render_template("Pizza.html")

if __name__ == "__main__":
    app.run(debug=False)
