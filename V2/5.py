from bottle import route, run

@route('/stevejobs')
def stevejobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<body>" \
           "<a href='localhost:8080/biography'>Biography</a><br>" \
           "<a href='localhost:8080/pictures'>Pictures</a><br>"  \
           "Steve Jobs er kúl \n <h2>Hann er frægur</h2>" \
           "</body>" \
           "</html>"

@route('/biography')
def biography():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<body>" \
           "<a href='localhost:8080/stevejobs'>Steve Jobs</a><br>" \
           "<a href='localhost:8080/pictures'>Pictures</a><br>" \
           "Hann var fæddur í San Francisco" \
           "</body>" \
           "</html>"

@route('/pictures')
def pictures():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<body>" \
           "<a href='localhost:8080/stevejobs'>Steve Jobs</a><br>" \
           "<a href='localhost:8080/biography'>Biography</a><br>" \
           "Það er ekki til mynd af Steve Jobs<br>" \
           "<input type='checkbox' name='check' value='Check'>Hakaðu við kassann ef þú vilt sjá myndir hér :)<br>" \
           "<input type='submit' value='Submit'>" \
           "</body>" \
           "</html>"


run(host='localhost', port=8080, debug=True)