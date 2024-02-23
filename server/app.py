from flask import Flask, render_template, request, url_for, jsonify,redirect
from os.path import join


app = Flask(__name__)
# routes = "home", "estoque", "cadastro", "financeiro",
routes = "home", "estoque"


@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "GET":
        return render_template("index.html",title_page="Login")
    
    if request.method == "POST":
        user_email = request.form["useremail"]
        user_password = request.form["userpassword"]
        if user_email == "mateussiilva" and user_password == "3010":
            return redirect(url_for("home"))


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html",title_page="Pagina Inicial",routes=routes)

@app.route("/estoque")
def estoque():
    return render_template("estoque.html",title_page="Estoque"), 200


if __name__ == "__main__":
    app.run(debug=True)
