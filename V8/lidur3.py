import bottle
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@bottle.route("/")
def index():
    return "<a href='/add/1'>Vara 1</a><br>" \
           "<a href='/add/2'>Vara 2</a><br>" \
           "<a href='/add/3'>Vara 3</a><br>" \
           "<a href='/add/4'>Vara 4</a><br>" \
           "<a href='/checkout'><b>Karfa</b></a>"

@bottle.route("/add/<item>")
def add(item):
    session = bottle.request.environ.get('beaker.session')
    session[item] = "Vara"+item
    session.save()
    bottle.redirect("/")

@bottle.route("/checkout")
def checkout():
    session = bottle.request.environ.get('beaker.session')
    for i in range(1,5):
        if session[str(i+1)] == "Vara"+str(i+1):
            return session[str(i)]+"<br>"
    return "<a href='/'>Halda áfram að versla</a><br>" \
           "<a href='/delete'>Eyða öllu úr körfu</a>"

@bottle.route("/delete")
def delete():
    session = bottle.request.environ.get('beaker.session')
    session.delete()
    bottle.redirect("/")

bottle.run(app=app)