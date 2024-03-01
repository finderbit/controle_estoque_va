from flask import Flask, render_template, request, url_for, jsonify,redirect
from bps.login import bp_login
from bps.cadastro import bp_cadastro


app = Flask(__name__)
app.register_blueprint(bp_login)
app.register_blueprint(bp_cadastro)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/resultado")
def result():
    return "Pessoa Cadastrada com sucesso "
    


if __name__ == "__main__":
    app.run(debug=True)
