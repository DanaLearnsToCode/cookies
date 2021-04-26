import os
import time


from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    t0 = time.time()
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["question1"]=request.form['question1'] 
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["question2"]=request.form['question2']
    return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    t1 = time.time()
    total = t1-t0
    session["question3"]=request.form['question3']
    return render_template('page4.html')










if __name__=="__main__":
    app.run(debug=False)
