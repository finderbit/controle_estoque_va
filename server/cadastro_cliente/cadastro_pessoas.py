from flask import Blueprint, render_template, request,redirect,url_for
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
        cliente = request.form["cliente"]
        bairro = request.form["bairro"]
        # rua = request.form["rua"]
        # cidade = request.form["cidade"]
        tel = request.form["tel"]
        print(tel)
        # receber_dados(cliente,bairro,tel)
        
        return render_template("cadastro_pessoa.html")
    elif request.method == "GET":
        return render_template("cadastro_pessoa.html")
