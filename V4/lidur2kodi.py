from bottle import run,route,template,static_file

@route("/<name>")
def name(name = "a"):
    if name != "" and name != "1" and name != "2" and name != "3" and name != "4":
        return "Röng undir síða"

@route("/")
def index():
    return "<a href='1'>CSC, HPE Enterprise Services Merge To Form DXC</a><br><br>" \
           "<a href='2'>Nato chief: world is at its most dangerous point in a generation</a><br><br>" \
           "<a href='3'>BlackRock cuts PMs and fees in active equity overhaul</a><br><br>" \
           "<a href='4'>UK lawmakers approve EU withdrawal bill</a>"

@route("/<tala>")
def frettir(tala = "1"):
    return template(str(tala))

@route('/css2/<filename:re:.*\.css>')
def css(filename):
       return static_file(filename, root='./css2')


@route('/images2/<filename:re:.*\.jpg>')
def image(filename):
    return static_file(filename, root='./images2', mimetype='image/jpg')

run(host='localhost', port=8080)