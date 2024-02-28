from flask import Flask

app = Flask(__name__)
@app.route('/')
def viewPage():
    nome = "sla"
    dados = {"profissao":"dev", "idade": 1}
    return render_template("index.html", nome=nome, dados=dados)
