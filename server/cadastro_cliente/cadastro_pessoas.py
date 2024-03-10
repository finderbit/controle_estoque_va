from flask import Blueprint, render_template, request, redirect, url_for
# from main import receber_dados

bp_cadastro = Blueprint("cadastro_cliente", __name__)


""" 
cliente == cliente
rua == rua
bairro == bairro
cidade == cidade
tel == telefone



"""


@bp_cadastro.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nameclient"]
        cpf = request.form["cpfclient"]
        rua = request.form["rua"]
        numero = request.form["numero"]
        bairro = request.form["bairro"]
        # print(nome, cpf, rua, numero, bairro)
        print(nome)
        return render_template("cadastro_pessoa.html", title_page="Cadastro de Cliente")
    elif request.method == "GET":
        return render_template("cadastro_pessoa.html", title_page="Cadastro de Cliente")
