# from flask import Flask, render_template, request, session
# from classes.author import Author
# from classes.awards import Awards
# from classes.book import Books
# from classes.bookawards import Books_Awards
# from datafile import filename

# app = Flask(__name__)
# app.secret_key = 'BAD_SECRET_KEY'

# Author.read(filename + 'Publishing.db')
# Awards.read(filename + 'Publishing.db')

# prev_option_authors = ""
# prev_option_awards = ""

# @app.route("/author", methods=["POST", "GET"])
# def authors():
#     global prev_option_authors
#     butshow, butedit = "enabled", "disabled"
#     option = request.args.get("option")

#     if option == "edit":
#         butshow, butedit = "disabled", "enabled"
#     elif option == "delete":
#         obj = Author.current()
#         Author.remove(obj.id)
#         if not Author.previous():
#             Author.first()
#     elif option == "insert":
#         butshow, butedit = "disabled", "enabled"
#     elif option == 'cancel':
#         pass
#     elif prev_option_authors == 'insert' and option == 'save':
#         strobj = str(Author.get_id(0)) + ';' + request.form["_authors_name"] + ';' + \
#                  request.form["_nationality"] + ';' + request.form["_birth_year"] + ';' + \
#                  request.form["_royalty_percentage"]
#         obj = Author.from_string(strobj)
#         Author.insert(obj.id)
#         Author.last()
#     elif prev_option_authors == 'edit' and option == 'save':
#         obj = Author.current()
#         obj._authors_name = request.form["_authors_name"]
#         obj._nationality = request.form["_nationality"]
#         obj._birth_year = int(request.form["_birth_year"])
#         obj._royalty_percentage = float(request.form["_royalty_percentage"])
#         Author.update(obj.id)
#     elif option == "first":
#         Author.first()
#     elif option == "previous":
#         Author.previous()
#     elif option == "next":
#         Author.nextrec()
#     elif option == "last":
#         Author.last()
#     elif option == 'exit':
#         return "<h1>Thank you for using this app</h1>"

#     prev_option_authors = option
#     obj = Author.current()

#     if option == 'insert' or len(Author.lst) == 0:
#         id = Author.get_id(0)
#         _authors_name = _nationality = _birth_year = _royalty_percentage = ""
#     else:
#         id = obj.id
#         _authors_name = obj._authors_name
#         _nationality = obj._nationality
#         _birth_year = obj._birth_year
#         _royalty_percentage = obj._royalty_percentage

#     return render_template("index.html", tipo="author", butshow=butshow, butedit=butedit,
#                            id=id, _authors_name=_authors_name, _nationality=_nationality,
#                            _birth_year=_birth_year, royalty_percentage=_royalty_percentage,
#                            ulogin=session.get("user"))


# @app.route("/awards", methods=["POST", "GET"])
# def awards():
#     global prev_option_awards
#     butshow, butedit = "enabled", "disabled"
#     option = request.args.get("option")

#     if option == "edit":
#         butshow, butedit = "disabled", "enabled"
#     elif option == "delete":
#         obj = Awards.current()
#         Awards.remove(obj.id)
#         if not Awards.previous():
#             Awards.first()
#     elif option == "insert":
#         butshow, butedit = "disabled", "enabled"
#     elif option == 'cancel':
#         pass
#     elif prev_option_awards == 'insert' and option == 'save':
#         strobj = str(Awards.get_id(0)) + ';' + request.form["_id"] + ';' + request.form["_name"]
#         obj = Awards.from_string(strobj)
#         Awards.insert(obj._id)
#         Awards.last()
#     elif prev_option_awards == 'edit' and option == 'save':
#         obj = Awards.current()
#         obj._awards_id = request.form["_awards_id"]
#         obj._award_name = request.form["_award_name"]
#         Awards.update(obj.id)
#     elif option == "first":
#         Awards.first()
#     elif option == "previous":
#         Awards.previous()
#     elif option == "next":
#         Awards.nextrec()
#     elif option == "last":
#         Awards.last()
#     elif option == 'exit':
#         return "<h1>Thank you for using this app</h1>"

#     prev_option_awards = option
#     obj = Awards.current()

#     if option == 'insert' or len(Awards.lst) == 0:
#         id = Awards.get_id(0)
#         _awards_id = _award_name = ""
#     else:
#         id = obj.id
#         _awards_id = obj._awards_id
#         _award_name = obj._award_name

#     return render_template("index.html", tipo="awards", butshow=butshow, butedit=butedit,
#                            id=id, _awards_id=_awards_id, _award_name=_award_name,
#                            ulogin=session.get("user"))




# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=False)


from flask import Flask, render_template, request, session
from classes.author import Author
from classes.awards import Awards
from classes.book import Books
from classes.bookawards import Books_Awards
from datafile import filename
from classes.userlogin import Userlogin
from subs.apps_plot import apps_plot



Userlogin.read(filename + 'users.db')
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

Author.read(filename + 'Publishing.db')
Awards.read(filename + 'Publishing.db')
Books.read(filename + 'Publishing.db')
Books_Awards.read(filename + 'Publishing.db')

prev_option_authors = ""
prev_option_awards = ""
prev_option_books = ""
prev_option_books_awards = ""
prev_option = ""


@app.route("/author", methods=["POST", "GET"])
def authors():
    global prev_option_authors
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
    elif prev_option_authors == 'insert' and option == 'save':
        strobj = str(Author.get_id(0)) + ';' + request.form["_authors_name"] + ';' + \
                 request.form["_nationality"] + ';' + request.form["_birth_year"] + ';' + \
                 request.form["_royalty_percentage"]
        obj = Author.from_string(strobj)
        Author.insert(obj.id)
        Author.last()
    elif prev_option_authors == 'edit' and option == 'save':
        obj = Author.current()
        obj._authors_name = request.form["_authors_name"]
        obj._nationality = request.form["_nationality"]
        obj._birth_year = int(request.form["_birth_year"])
        obj._royalty_percentage = float(request.form["_royalty_percentage"])
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

    prev_option_authors = option
    obj = Author.current()

    if option == 'insert' or len(Author.lst) == 0:
        id = Author.get_id(0)
        _authors_name = _nationality = _birth_year = _royalty_percentage = ""
    else:
        id = obj.id
        _authors_name = obj._authors_name
        _nationality = obj._nationality
        _birth_year = obj._birth_year
        _royalty_percentage = obj._royalty_percentage

    return render_template("index.html", tipo="author", butshow=butshow, butedit=butedit,
                           id=id, _authors_name=_authors_name, _nationality=_nationality,
                           _birth_year=_birth_year, royalty_percentage=_royalty_percentage,
                           ulogin=session.get("user"))


@app.route("/awards", methods=["POST", "GET"])
def awards():
    global prev_option_awards
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Awards.current()
        Awards.remove(obj.id)
        if not Awards.previous():
            Awards.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_awards == 'insert' and option == 'save':
        strobj = str(Awards.get_id(0)) + ';' + request.form["_awards_id"] + ';' + request.form["_award_name"]
        obj = Awards.from_string(strobj)
        Awards.insert(obj._id)
        Awards.last()
    elif prev_option_awards == 'edit' and option == 'save':
        obj = Awards.current()
        obj._awards_id = request.form["_awards_id"]
        obj._award_name = request.form["_award_name"]
        Awards.update(obj.id)
    elif option == "first":
        Awards.first()
    elif option == "previous":
        Awards.previous()
    elif option == "next":
        Awards.nextrec()
    elif option == "last":
        Awards.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_awards = option
    obj = Awards.current()

    if option == 'insert' or len(Awards.lst) == 0:
        id = Awards.get_id(0)
        _awards_id = _award_name = ""
    else:
        id = obj.id
        _awards_id = obj._awards_id
        _award_name = obj._award_name

    return render_template("index.html", tipo="awards", butshow=butshow, butedit=butedit,
                            id=id, _awards_id=_awards_id, _award_name=_award_name,
                            ulogin=session.get("user"))


@app.route("/books", methods=["POST", "GET"])
def books():
    global prev_option_books
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Books.current()
        Books.remove(obj.id)
        if not Books.previous():
            Books.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_books == 'insert' and option == 'save':
        strobj = str(Books.get_id(0)) + ';' + request.form["_books_title"] + ';' + \
                  request.form["_genre"] + ';' + request.form["_publication_year"]
        obj = Books.from_string(strobj)
        Books.insert(obj.id)
        Books.last()
    elif prev_option_books == 'edit' and option == 'save':
        obj = Books.current()
        obj._books_title = request.form["_books_title"]
        obj._genre = request.form["_genre"]
        obj._publication_year = int(request.form["_publication_year"])
        Books.update(obj.id)
    elif option == "first":
        Books.first()
    elif option == "previous":
        Books.previous()
    elif option == "next":
        Books.nextrec()
    elif option == "last":
        Books.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_books = option
    obj = Books.current()

    if option == 'insert' or len(Books.lst) == 0:
        id = Books.get_id(0)
        _books_title = _genre = _publication_year = ""
    else:
        id = obj.id
        _books_title = obj._books_title
        _genre = obj._genre
        _publication_year = obj._publication_year

    return render_template("index.html", tipo="books", butshow=butshow, butedit=butedit,
                            id=id, _books_title=_books_title, _genre=_genre,
                            _publication_year=_publication_year, ulogin=session.get("user"))


@app.route("/books_awards", methods=["POST", "GET"])
def books_awards():
    global prev_option_books_awards
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Books_Awards.current()
        Books_Awards.remove(obj.id)
        if not Books_Awards.previous():
            Books_Awards.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_books_awards == 'insert' and option == 'save':
        strobj = str(Books_Awards.get_id(0)) + ';' + request.form["_awards_id"] + ';' + \
                  request.form["_books_id"] + ';' + request.form["_year"]
        obj = Books_Awards.from_string(strobj)
        Books_Awards.insert(obj.id)
        Books_Awards.last()
    elif prev_option_books_awards == 'edit' and option == 'save':
        obj = Books_Awards.current()
        obj._awards_id = int(request.form["_awards_id"])
        obj._books_id = int(request.form["_books_id"])
        obj._year = int(request.form["_year"])
        Books_Awards.update(obj.id)
    elif option == "first":
        Books_Awards.first()
    elif option == "previous":
        Books_Awards.previous()
    elif option == "next":
        Books_Awards.nextrec()
    elif option == "last":
        Books_Awards.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_books_awards = option
    obj = Books_Awards.current()

    if option == 'insert' or len(Books_Awards.lst) == 0:
        id = Books_Awards.get_id(0)
        _awards_id = _books_id = _year = ""
    else:
        id = obj.id
        _awards_id = obj._awards_id
        _books_id = obj._books_id
        _year = obj._year

    return render_template("index.html", tipo="books_awards", butshow=butshow, butedit=butedit,
                            id=id, _awards_id=_awards_id, _books_id=_books_id, _year=_year,
                            ulogin=session.get("user"))
@app.route("/")
def index():
    return render_template("index1.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return render_template("login.html", id= 0, user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/plot", methods=["POST", "GET"])
def plot():
    return apps_plot()

# @app.route("/plotly", methods=["POST", "GET"])
# def plotly():
#     return apps_plotly()



@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index1.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index1.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    msg = ""
    ulogin=session.get("user")
    if (ulogin != None):
        user_id = Userlogin.get_user_id(ulogin)
        group = Userlogin.obj[user_id].usergroup
        if group != "admin":
            Userlogin.current(user_id)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            if obj.id != user_id:
                Userlogin.remove(obj.id)
                if not Userlogin.previous():
                    Userlogin.first()
            else:
                msg = 'You cannot delete the same user'
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            user = request.form["user"]
            if len(Userlogin.find(user, 'user')) == 0:
                usergroup = request.form["usergroup"]
                password =  request.form["password"]
                obj = Userlogin(0, user, usergroup, Userlogin.set_password(password))
                Userlogin.insert(obj.id)
                Userlogin.last()
            else:
                msg = 'duplicate username'
                Userlogin.current()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
            Userlogin.update(obj.id)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index1.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            id = 0
            user = ""
            usergroup = ""
            password = ""
        else:
            id = obj.id
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, msg=msg,id=id, user=user,
                               usergroup = usergroup,password=password,ulogin=session.get("user"), group=group)
    else:
        return render_template("index1.html", ulogin=ulogin)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)