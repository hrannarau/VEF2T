from bottle import route, run

@route('/verkefni2.2')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)