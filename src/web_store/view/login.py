from flask import Blueprint
from flask import session, render_template, request
from flask import url_for, redirect

view_login=Blueprint("view_login", __name__)

@view_login.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        session["usuario"]=request.form["username"]
        return redirect(url_for('view_login.home'))
    else: 
        if "usuario" in session:
            return redirect(url_for('view_login.home'))
        return render_template('login.html', title='Login')
    
@view_login.route('/')
def index():
    if "usuario" in session:
        return home()
    return render_template('login.html', title='Login')

    

@view_login.route('/home') # Página de inicio
def home():
    if "usuario" in session:
        return render_template('home.html')
    return render_template('login.html', title='Login')