from bottle import route, request, response, run, template
@route("/verkefni2.3")
def hallo():
    return "<h2>Halló heimur!</h2>"
run(host='localhost', port=8080, debug=True)