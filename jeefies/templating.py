import jinja2 as jj
import os

conf = {'path': os.path.join(os.getcwd(), 'static')}
def config(tplpath):
    conf['path'] = os.path.abspath(tplpath)

def _env():
    g = conf.get('env')
    if g:
        return g
    else:
        tpll = jj.FileSystemLoader(conf.get('path') or '.')
        tple = jj.Environment(loader=tpll)
        conf['env'] = tple
        return _env()

def render(filename, **context):
    return _env().get_template(filename).render(context)
