from flask import Blueprint, render_template, request,redirect,url_for
from main import receber_dados

bp_cadastro = Blueprint("cadastro", __name__, url_prefix="/cadastro")


""" 
cliente == cliente
rua == rua
bairro == bairro
cidade == cidade
tel == telefone



"""


@bp_cadastro.route("/cliente", methods=["POST", "GET"])
def cadastrar_pessoa():
    if request.method == "POST":
        cliente = request.form["cliente"]
        bairro = request.form["bairro"]
        # rua = request.form["rua"]
        # cidade = request.form["cidade"]
        tel = request.form["tel"]
        receber_dados(cliente,bairro,tel)
        
        return render_template("cadastro_pessoa.html")
    elif request.method == "GET":
        return render_template("cadastro_pessoa.html")
