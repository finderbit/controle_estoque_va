from flask import Blueprint,render_template


bp_vendas = Blueprint("vendas",__name__)


@bp_vendas.route("/vendas")
def vendas():
    return render_template("vendas.html")

