from flask import Flask, render_template, request, url_for
from os.path import join
from server.main import readjson

app = Flask(__name__)
routes = "home", "estoque", "cadastro", "financeiro",


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", routes=routes,title_page="ERP FINDERBIT"), 200

@app.route("/estoque")
def estoque():
    return render_template("estoque.html", routes=routes, title_page="Estoque"), 200

if __name__ == "__main__":
    app.run(debug=True)
