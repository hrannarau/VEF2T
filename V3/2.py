from bottle import route, run, template, static_file, request

@route('/')
def myndir():
    forum_id = request.query.id
    page = request.query.page
    id = forum_id
    for i in range(10):
        if id==str(i):
            return "<!DOCTYPE html>" \
                   "<html>" \
                   "<head>" \
                   "<link rel='stylesheet' type='text/css' href='/css2/stylesheet.css'>" \
                   "</head" \
                   "<body>" \
                   "<p>halló</p>" \
                   "<a href='/'>Smelltu hér til að fara til baka</a>" \
                   "</body>" \
                   "</html>"

    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "<link rel='stylesheet' type='text/css' href='/css2/stylesheet.css'>" \
           "</head" \
           "<body>" \
           "<a href='?id=1'><img src='/tolur/1.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=2'><img src='/tolur/2.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=3'><img src='/tolur/3.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=4'><img src='/tolur/4.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=5'><img src='/tolur/5.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=6'><img src='/tolur/6.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=7'><img src='/tolur/7.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=8'><img src='/tolur/8.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=9'><img src='/tolur/9.jpg' style='width:400px;height:400px'></a>'" \
           "<a href='?id=10'><img src='/tolur/10.jpg' style='width:400px;height:400px'></a>'" \
           "</body>" \
           "</html>"



@route('/tolur/<filename:re:.*\.jpg>')
def image(filename):
    return static_file(filename, root='./tolur', mimetype='image/jpg')

@route('/css2/<filename:re:.*\.css>')
def css(filename):
       return static_file(filename, root='./css2')

run(host='localhost', port=8080)