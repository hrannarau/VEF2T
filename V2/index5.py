from bottle import route, run

@route('/verkefni2.5/stevejobs')
def stevejobs():
    return "Steve Jobs er kúl \n <h2>Hann er frægur</h2>"

@route('/verkefni2.5/biography')
def biography():
    return "Hann var fæddur í San Francisco"

@route('/verkefni2.5/pictures')
def pictures():
    return "Það er ekki til mynd af Steve Jobs"
run(host='localhost', port=8080, debug=True)