from login import cookie_req
from login import testper
from flask import current_app
import os
from flask import url_for, Flask, render_template, redirect, session, flash, request, make_response
req = request
mkresp = make_response

app = Flask(__name__)

app.config["CONPATH"] = os.getcwd()


@app.route('/')
def index():
    return 'index'


@app.route('/url/<name>')
def onearg(name):
    return name


@app.route('/url/<name>/<n>')
def twoarg(name, n):
    return '.'.join([name, n])


@app.route('/t1')
def red1():
    return redirect(url_for('onearg', name='name'))


@app.route('/t2')
def red2():
    return redirect(url_for('twoarg', name='name', n='n'))


@app.route("/configs")
def conf():
    cac, aac = current_app.config, app.config
    print(cac, aac)
    return "<p>{}</p><h1>conf</h1><p>{}</p>".format(cac.get("CONPATH"), aac.get("CONPATH"))


@app.route('/pert')
@testper(16, lambda: 'permission denined')
def pert():
    return 'has per'


@app.route('/addc')
def addcook():
    resp = mkresp('add cookie {name: here}')
    resp.set_cookie('name', 'here')
    return resp


@app.route('/addc/<name>')
def adc(name):
    resp = mkresp('add cookie {0}: j'.format(name))
    resp.set_cookie(name, 'j')
    return resp


@app.route('/cr')
@cookie_req('name', 'here', lambda: 'no c')
def cook_req():
    return 'has cookie'


@app.route('/cr/<name>')
@cookie_req('name', 'j', lambda: 'no c')
def creq(name):
    return 'has cookie {}'.format(name)


if __name__ == '__main__':
    app.run(port=5400, host='0.0.0.0')
