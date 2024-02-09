from flask import Flask, render_template, request, url_for


app = Flask(__name__)


routes = "home", "financeiro", "estoque"


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





if __name__ == "__main__":
    app.run(debug=True)
