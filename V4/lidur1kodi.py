from bottle import route,run,template,static_file

@route("/<name>")
def index(name = "stevejobs"):
    if name == "stevejobs":
        return template("stevejobs")
    elif name == "biography":
        return template("bio")
    elif name == "pictures":
        return template("pics")
    else:
        return "Röng undir síða"

@route('/css/<filename:re:.*\.css>')
def css(filename):
       return static_file(filename, root='./css')

@route('/images/<filename:re:.*\.jpg>')
def image(filename):
    return static_file(filename, root='./images', mimetype='image/jpg')

run(host='localhost', port=8080)