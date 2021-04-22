from flask import Flask
from flask import render_template, request

#estou importando tudo
import Aluno
#estou importando parcialmente
#from Aluno import Professor

# não parece como app é a instância de um objeto 
# da classe Flask

app = Flask(__name__)

#route é um método da classe Flask
# decorador é uma função que adiciona
# poderes para o método olá
@app.route("/")
def ola():
    return render_template("index2.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        registro = user + " - " + senha

        print (registro)

        arquivo = open("registros.txt","r")
        lista = arquivo.readlines()

        #quero ver se registro está na lista
        print (lista)

        if (registro in lista):
            return "<h1>Login efetuado com sucesso</h1>"
            # render_template("disciplinas.html")
        else:
            return "<h1>Login Mal sucedido</h1>"

        return "<h1>Login efetuado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

@app.route("/cadastro")
def hello():
    return render_template('index3.html')

@app.route("/registro", methods = ["POST", "GET"])
def registro():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == " " or senha == " ":
            return "<h1>Por favor cadastre user e senha</h1>"

        #verificar se a variável user tem uma letra
        #maiúscula

        registro = user + " - " + senha 
        
        print (registro)

        arquivo = open("registros.txt","a")
        arquivo.writelines(registro)

        return "<h1>Cadastro realizado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

app.run()