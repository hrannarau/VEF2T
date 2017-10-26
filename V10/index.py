from bottle import *
import pymysql

@route("/")
def index():
    return template("template.tpl")

@route("/send", method= "POST")
def send():
    connect = pymysql.connect(user="1612002390", passwd="mypassword", host="tsuts.tskoli.is", port=3306,database="1612002390_v10")

    username = request.forms.get("username")
    passwd = request.forms.get("password")
    with connect.cursor() as cursor:
        try:
            sql = "INSERT INTO `user` (`user`,`pass`) VALUES (%s,%s)"
            cursor.execute(sql,(username,passwd))
            connect.commit()
            return "Thank you for signing up<br>" \
                   "Your username is:" + username+\
                   "<br>Click <a href='/login'>here</a> to login"
        except pymysql.err.IntegrityError:
            return "This username is already taken :(<br>" \
                   "<a href='/'>Click here to go back</a>"

@route("/login")
def login():
    return template("login.tpl")

@route("/leyni", method="POST")
def leyni():
    connect = pymysql.connect(user="1612002390", passwd="mypassword", host="tsuts.tskoli.is", port=3306,database="1612002390_v10")
    username = request.forms.get("username")
    passwd = request.forms.get("password")
    with connect.cursor() as cursor:
        sql = "select * from `user` where `user`=%s and `pass`=%s;"
        if cursor.execute(sql, (username,passwd)):
            return "Welcome: "+username
        else:
            return "Login failed<br>" \
                   "Click <a href='/login'>here</a> to go back to login"

run(host='localhost', port=8080)