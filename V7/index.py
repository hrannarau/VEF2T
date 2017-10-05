from bottle import route,response,run,request,redirect,error

@error(405)
def error405(error):
    return "Þú verður að skrá þig inn fyrst<br>" \
           "<a href='/'>Veldu hér til að skrá þig inn</a>"

@route("/")
def login():
    response.set_cookie("account", "", expires=0)
    return "<form action='/post' method='post'>" \
                "<label>Username:</label><br>" \
                "<input type='text' name='username'><br>" \
                "<label>Password:</label><br>" \
                "<input type='password' name='password'><br>" \
                "<input type='submit' value='Login'>" \
           "</form>"

@route("/post", method='POST')
def index():
    realusername = 'username'
    realpassword = 'password'
    def check_login(a,b):
        if a == realusername and b == realpassword:
            return True
        else:
            return False
    username = request.forms.get("username")
    password = request.forms.get("password")

    if check_login(username,password):
        response.set_cookie("account", username, secret="lol")
        return "Successfully logged in<br>" \
               "Press <a href='/'>here</a> to go back to login"
    else:
        return "Login failed<br>" \
               "Click <a href='/'>here</a> to go back to login"



run(host='localhost', port=808, debug=True)
