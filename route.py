from flask import Flask
from flask import render_template
from flask import request
from pprint import pprint
import os
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
STATIC_DIR = os.path.abspath('../static')
@app.route('/')
def dashboard():
   
   return render_template('halaman_regresi.html')

@app.route('/cek',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      tinggi = request.form['tinggi']
      jk = request.form['jk']
      nama = request.form['nama']
      return render_template('halaman_regresi.html',isi=isi)


if __name__ == '__main__':
   app.run(debug = True)