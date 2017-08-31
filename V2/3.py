from bottle import route, request, response, run, template
@route("/verkefni2.3")
def hallo():
    return "<DOCTYPE html>" \
           "<html>" \
           "<body>" \
           "<h2>Halló heimur!</h2>" \
           "</body>" \
           "</html>"
run(host='localhost', port=8080, debug=True)