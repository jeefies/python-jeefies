from flask_mail import Message
import os
import hashlib
from flask import current_app as ca
from jeefies import Hexsec
from jeefies import Content
from functools import wraps
from flask import url_for, Flask, render_template, redirect, session, flash, request, make_response
req = request
mkresp = make_response


def origerror():
    """default error for the protect"""
    flash('Please login')
    try:
        return redirect('main.index')
    except:
        return redirct("index")


def protect(error=origerror, conpath=os.getcwd()):
    """A decorator to decarate a website need to login(protect)"""
    def _protect(func):
        @wraps(func)
        def __protect(*args, **kwargs):
            #print(args, kwargs)
            name = req.cookies.get('name' + req.remote_addr)
            # print(name)
            con = Content(conpath, 'user')
            # print(con.allitem())
            if con.has(name):
                return func(*args, **kwargs)
            else:
                #print('has no such user?')
                return error()
        return __protect
    return _protect


def cookie_req(requires: tuple(('name', 'content')), error=origerror):
    """a wraped function to check whether the cookie is exists or not"""
    def _cookie(func):
        @wraps(func)
        def __cookie(*args, **kwargs):
            # print(args, kwargs) no args, only kwargs
            cookies = requires[:2]
            cookie, cont = cookies
            res = func(*args, **kwargs)
            if cookie in kwargs.keys():
                cook = req.cookies.get(kwargs[cookie])
            else:
                cook = req.cookies.get(cookie)
            if cont in kwargs.keys():
                cont = kwargs[cont]
            #print(cook, cont)
            if not isinstance(cook, type(cont)) or cook != cont:
                return error()
            else:
                return res
        return __cookie
    return _cookie


def Login(returned, name, passwd, conpath=os.getcwd()):
    con = Content(conpath, 'user')
    print(con.get(name))
    if con.has(name) and Hexsec.decrypt(con.get(name)[1][0]) == passwd:
        pass
    else:
        print('eeee')
        flash('No such user')
        return redirect('/')
    resp = mkresp(returned)
    resp.set_cookie('name' + req.remote_addr, name)
    resp.set_cookie('passwd' + req.remote_addr, passwd)
    session[req.remote_addr] = name
    return resp


def Logout(returned):
    name = session.get(req.remote_addr, None)
    resp = mkresp(returned)
    resp.delete_cookie('name' + req.remote_addr)
    resp.delete_cookie('passwd'+req.remote_addr)
    session.pop(name, None)
    return resp


def get_user(conpath=os.getcwd()):
    name = req.cookies.get('name'+req.remote_addr)
    return name


def permission(per, error=origerror, conpath=os.getcwd()):
    con = Content(conpath, 'user')

    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            fun = func(*args, **kwargs)
            user = get_user()
            res = con.get(user)
            if res is None or not res[1][1] == str(per):
                print(res[1][-1], per, res)
                return error()
            else:
                return func(*args, **kwargs)
        return __permission
    return _permission


def testper(permission, error=origerror):
    user = Content(os.getcwd(), 'user').get('name')

    def _per(func):
        @wraps(func)
        def __per(*a, **kw):
            if user[1][-1] != str(permission):
                print(permission, user[1][-1])
                return error()
            else:
                return func(*a, **kw)
        return __per
    return _per


def gravatar(email, size=100, default='identicon', rating='g'):
    url = 'https://secure.gravatar.com/avatar'
    hashs = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f'{url}/{hashs}?s={size}&d={default}&r={rating}'


def emailmsg(to, subject, tem, **kwargs):
    msg = Message(subject, sender=(
        'jeefy', 'jeefy163@163.com'), recipients=[to])
    msg.body = render_template(tem+'.txt', **kwargs)
    msg.html = render_template(tem+'.html', **kwargs)
    return msg
