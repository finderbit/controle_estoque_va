from flask import Blueprint


bp_login = Blueprint("login",__name__)

@bp_login.route("/login")
def login():
    return "Bem vindo a pagina de login"