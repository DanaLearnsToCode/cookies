import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('home.html')











if __name__=="__main__":
    app.run(debug=False)
