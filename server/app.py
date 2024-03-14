from flask import Flask
from login.login import bp_login
from cadastro_cliente.cadastro_pessoas import bp_cadastro
from home.index import bp_index
from vendas.vendas import bp_vendas


app = Flask(__name__)
app.register_blueprint(bp_index)
app.register_blueprint(bp_vendas)
app.register_blueprint(bp_login)
app.register_blueprint(bp_cadastro)


if __name__ == "__main__":
    app.run(debug=True)
