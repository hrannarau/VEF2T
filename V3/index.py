from bottle import route, run, template, static_file

@route('/<name>')
def index(name = 'stevejobs'):
    if name == 'stevejobs':
        return "<!DOCTYPE html>" \
               "<head>" \
               "<link rel='stylesheet' type='text/css' href='/css/main.css'" \
               "<meta charset='utf-8' />" \
               "</head>" \
               "<html>" \
               "<body>" \
               "<section>" \
               "<ul>" \
               "<li><a href='biography'>Biography</a></li><br><br>" \
               "<li><a href='pictures'>Pictures</a></li><br><br>" \
               "</ul>"  \
               "<p>Steve Jobs er kúl \n <h2>Hann er frægur</h2></p><br>" \
               "</section>" \
               "<img src='/images/stevejobs.jpg'>" \
               "</body>" \
               "</html>"
    elif name == 'biography':
        return "<!DOCTYPE html>" \
               "<html>" \
               "<head>" \
               "<link rel='stylesheet' type='text/css' href='/css/main.css'" \
               "<meta charset='utf-8' />" \
               "</head>" \
               "<body" \
               "<section>" \
               "<ul>" \
               "<li><a href='stevejobs'>Steve Jobs</a></li><br><br>" \
               "<li><a href='pictures'>Pictures</a></li><br><br>" \
               "</ul" \
               "<p>Hann var fæddur í San Francisco</p><br><br>" \
               "</section>" \
               "<img src='/images/billgates.jpg'>" \
               "</body>" \
               "</html>"
    elif name == 'pictures':
        return "<!DOCTYPE html>" \
               "<html>" \
               "<head>" \
               "<link rel='stylesheet' type='text/css' href='/css/main.css'" \
               "<meta charset='utf-8' />" \
               "</head>" \
               "<body>" \
               "<section>" \
               "<ul>" \
               "<li><a href='stevejobs'>Steve Jobs</a></li><br><br>" \
               "<li><a href='biography'>Biography</a></li><br><br>" \
               "</ul>" \
               "<p>Það er ekki til mynd af Steve Jobs</p><br>" \
               "</section>" \
               "<img src='/images/jeffbezos.jpg'>" \
               "</body>" \
               "</html>"
    else:
        return "Röng undirsíða"

@route('/css/<filename:re:.*\.css>')
def css(filename):
       return static_file(filename, root='./css')

@route('/images/<filename:re:.*\.jpg>')
def image(filename):
    return static_file(filename, root='./images', mimetype='image/jpg')

run(host='localhost', port=8080)