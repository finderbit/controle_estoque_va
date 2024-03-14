from flask import Blueprint, render_template, request, redirect, url_for
from json import load

bp_cadastro = Blueprint("cadastro_cliente", __name__)


def get_dados():
    with open("models/user.json","r") as fp:
        dados = load(fp)
    return dados



@bp_cadastro.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nameclient"]
        cpf = request.form["cpfclient"]
        rua = request.form["rua"]
        numero = request.form["numero"]
        bairro = request.form["bairro"]
        

        return render_template("cadastro_pessoa.html", title_page="Cadastro de Cliente",dados=get_dados())
    
    elif request.method == "GET":
        return render_template("cadastro_pessoa.html", title_page="Cadastro de Cliente",dados=get_dados())
