from flask import Flask, render_template, request, url_for
from os.path import join
from main import readjson

app = Flask(__name__)
routes = "home", "financeiro", "estoque","cadastro"
ROOT_MODEL = "models"
NAME_FILE = "clientes.json"
FILE = join(ROOT_MODEL,NAME_FILE)
dados = readjson(FILE)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", routes=routes), 200


@app.route("/financeiro")
def financeiro():
    return render_template("financeiro.html",routes=routes,title_page="Financeiro"), 200


@app.route("/estoque")
def estoque():
    return render_template("estoque.html",routes=routes,title_page="Estoque"), 200


@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "GET":
        # return dados
        return render_template("cadastro.html",
                               routes=routes,title_page="Cadastro",dados=dados), 200
    if request.method == "POST":
        return ""





if __name__ == "__main__":
    app.run(debug=True)
