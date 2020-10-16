from flask import url_for, Flask, render_template, redirect, session, flash, request, make_response
req = request
mkresp = make_response


def render(file, **kwargs):
    """A object to return rendered template with name=user_name argument"""
    name = req.cookies.get('name'+req.remote_addr)  # to get the user name
    if name:
        kwargs['name'] = name
    return render_template(file, **kwargs)
