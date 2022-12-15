
from flask import Flask, render_template,url_for
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__,static_url_path='/static')


@app.route('/')

def index():
  return render_template('index.html')
  
  
  
@app.route('/application')

def appli():
  return  render_template('app.html')
 
 

