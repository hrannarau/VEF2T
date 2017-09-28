from bottle import run, route, request,template
import csv

@route('/')
def index():
    return template("template.tpl")

@route("/send", method="POST")
def send():
    name = "Name: "+request.forms.get("name")
    username = "Username: "+request.forms.get("username")
    password = "Password: "+request.forms.get("password")
    number = "Telephone Number :"+request.forms.get("number")
    email = "Email Address: "+request.forms.get("email")
    listi = [name,username,password,number,email]
    splitter = ["------------------"]
    with open("users.csv","a") as rs:
        write = csv.writer(rs)
        for i in listi:
            write.writerow([i])
        write.writerow(splitter)
        return username+"<br>"\
               "<b>Thank You For Signing up!</b>"

run(host='localhost', port=8080)
