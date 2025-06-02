# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_login.py

"""""

from flask import Flask, render_template, request, session

#import das classes 
from classes.author import Author

prev_option = ""


def index(path):
    global prev_option
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")
    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Author.current()
        Author.remove(obj.id)
        if not Author.previous():
            Author.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option == 'insert' and option == 'save':
        strobj = str(Author.get_id(0))
        strobj = strobj + ';' + request.form["name"] + ';' + \
        request.form["dob"] + ';' + request.form["salary"]
        obj = Author.from_string(strobj)
        Author.insert(obj.id)
        Author.last()
    elif prev_option == 'edit' and option == 'save':
        obj = Author.current()
        obj.name = request.form["name"]
        obj.dob = request.form["dob"]
        obj.salary = float(request.form["salary"])
        Author.update(obj.id)
    elif option == "first":
        Author.first()
    elif option == "previous":
        Author.previous()
    elif option == "next":
        Author.nextrec()
    elif option == "last":
        Author.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"
    prev_option = option
    obj = Author.current()
    if option == 'insert' or len(Author.lst) == 0:
        id = 0
        id = Author.get_id(id)
        name = dob = salary = ""
    else:
        id = obj.id
        name = obj.name
        dob = obj.dob
        salary = obj.salary
    return render_template("index.html", butshow=butshow, butedit=butedit, 
                    id=id,name = name,dob=dob,salary=salary, 
                    ulogin=session.get("user"))

