from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("vision.html")

@app.route("/cadastro", methods = ["POST", "GET"])
def cadastro():
    #pegar os dados da visao
    #mandar os dados para o modelo
    user = ""
    senha = ""

    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            pessoa = model.Aluno(user,senha)
            pessoa.salva()
            return "<h1>Registro salvo com sucesso</h1>"

app.run()