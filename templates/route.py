from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
@app.route('/')
def dashboard():
   return render_template('halaman_regresi.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))


if __name__ == '__main__':
   app.run(debug = True)