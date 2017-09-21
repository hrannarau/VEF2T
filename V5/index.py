from bottle import run, route, request

@route('/')
def index():
    return "<!DOCTYPE html>" \
            "<html>" \
            "<head>" \
            "<link rel='stylesheet' type='text/css' href='/css/stylesheet.css'>"\
            "<meta charset='utf-8'>"\
            "</head>"\
            "<body>"\
            "<form action='/send' method='post'>"\
                "<h2>Upplýsingar um notanda</h2>"\
                "Nafn:<br>"\
                "<input type='text' name='name'><br>"\
                "Heimilisfang:<br>" \
                "<input type='text' name='address'><br>"\
                "Símanúmer:<br>" \
                "<input type='text' name='number' pattern='[0-9]{7}'><br>"\
                "Netfang:<br>" \
                "<input type='email' name='email'><br>"\
                "<h2>Pizzastærð</h2>"\
                "<input type='radio' name='size' value='9'> 9 tomma - 1000kr<br>"\
                "<input type='radio' name='size' value='12'> 12 tomma - 1500kr<br>"\
                "<input type='radio' name='size' value='18'> 18 tomma - 2000kr<br>" \
                "<br>" \
                "<h2>Val um álegg</h2>" \
                "Hvaða álegg má bjóða þér?<br><br>" \
                "Hvert álegg kostar 200 kr.<br><br>" \
                "<input type='checkbox' name='skinka'>Skinka.<br>" \
                "<input type='checkbox' name='ananas'>Ananas.<br>" \
                "<input type='checkbox' name='pepperoni'>Pepperoni.<br><br>" \
                "<input type='submit' value='Panta'>" \
            "</form>"\
            "</body>"\
            "</html>"

@route("/send", method="POST")
def post():
    name = request.forms.get("name")
    address = request.forms.get("address")
    number = request.forms.get("number")
    email = request.forms.get("email")
    staerd = request.forms.get("size")
    upphaed = 0
    if staerd == "9":
        staerd = "9 tommur"
        upphaed = upphaed + 1000
    elif staerd == "12":
        staerd = "12 tommur"
        upphaed = upphaed + 1500
    elif staerd == "18":
        staerd = "18 tommur"
        upphaed = upphaed + 2000
    skinka = request.forms.get("skinka")
    ananas = request.forms.get("ananas")
    pepperoni = request.forms.get("pepperoni")
    a = "Ekki skinka"
    b = "Ekki ananas"
    c = "Ekki pepperoni"
    if skinka == "on":
        a = "Skinka"
        upphaed = upphaed + 200
    if ananas == "on":
        b = "Ananas"
        upphaed = upphaed + 200
    if pepperoni == "on":
        c = "Pepperoni"
        upphaed = upphaed + 200
    vsk = upphaed*1.25
    vsk = "Virðisaukaskatturinn er: "+str(vsk)
    upphaed = "Heildarverð: "+str(upphaed)+" kr"
    return "Nafn: "+name+"<br>"+\
           "Heimilisfang: "+address+"<br>"+\
           "Símanúmer: "+number+"<br>"+\
           "Netfang: "+email+"<br>"+\
           "Stærð: "+staerd+"<br>"+\
           "Með:<br>"+\
           a+"<br>"+\
           b+"<br>"+\
           c+"<br>"+\
           upphaed+\
           "<br>"+\
           vsk

run(host='localhost', port=8080)