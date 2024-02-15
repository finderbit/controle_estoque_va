from flask import Flask, render_template, request, url_for,redirect
from main import writejson

app = Flask(__name__)
routes = "home", "estoque"
bd = "models/produtos.json"

produtos = [
    ["1", "Agua Mineral", "12", "2021", "12.70"],
    ["1", "Agua Mineral", "12", "2021", "12.70"],
]
iid = 0


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", routes=routes, title_page="Pagina Inicial"), 200

@app.route("/estoque", methods=["GET", "POST"])
def estoque():
    if request.method == "POST":
        req = {
            "nome":request.form["nome_do_produto"],
            "quantidade":request.form["quantidade_produto"],
            "ano":request.form["ano_de_fabricacao"],
            "valor":request.form["valor_produto"],
        }
        writejson(bd,req)
        return redirect(url_for("estoque"))

    return render_template("estoque.html", routes=routes, title_page="Estoque",produtos=produtos), 200


if __name__ == "__main__":
    app.run(debug=True)
