import os
import hashlib
from flask_mail import Message
try:
	from flask import render_template
except:
	import jinjia2
	def render_template(tpl_path, **kwargs):
		path, file = os.path.split(tpl_path)
		return jinjia2.Environment(
			loader = jinjia2.FileSystemLoader(path or './')
		).get_template(file).render(**kwargs)

def gravatar(email, size=256, default='identicon', rating='g'):
    url = 'https://secure.gravatar.com/avatar'
    hashs = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f'{url}/{hashs}?s={size}&d={default}&r={rating}'


def emailmsg(to, subject, tem, **kwargs):
    msg = Message(subject, sender=(
        'jeefy', 'jeefy163@163.com'), recipients=[to])
    msg.body = render_template(tem+'.txt', **kwargs)
    msg.html = render_template(tem+'.html', **kwargs)
    return msg
