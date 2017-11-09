from bottle import *

@route("/")
def index():
    return "Hallo"

run(host="0.0.0.0",port=argv[1])