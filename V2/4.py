from bottle import route, request, response, template, run
@route("/verkefni2.4")
def nafn():
    forum_id = request.query.id
    page = request.query.page
    id = forum_id
    if id == "1":
        return "Gunnar"
    elif id == "2":
        return "Daníel"
    elif id == "3":
        return "Þórarinn"
    else:
        return "ERROR"

run(host='localhost', port=8080, debug=True)