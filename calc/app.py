# Put your app in here.
from flask import Flask
from flask import request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_handler():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(add(a, b))

@app.route('/sub')
def sub_handler():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(sub(a, b))

@app.route('/mult')
def mult_handler():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(mult(a, b))

@app.route('/div')
def div_handler():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return str(div(a, b))

@app.route('/math/<operator>')
def math(operator):
  handler_dict = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
  }
  a = int(request.args['a'])
  b = int(request.args['b'])

  return str(handler_dict[operator](a, b))