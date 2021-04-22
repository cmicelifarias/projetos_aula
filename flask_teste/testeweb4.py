
#Controller
from flask import Flask
from flask import render_template, request

#estou importando tudo
#ainda não estou usando
import Aluno

app = Flask(__name__)

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
        
        #isso aqui vai mudar para o login de professor
        # e de aluno
        try: 
          arquivo = open("registros.txt","r")
          lista = arquivo.readlines()
        except IOError:
            print("Tentei colocar algo que não existe")
        except:
            print("deu erro aqui, o arquivo não existe")
        #quero ver se registro está na lista
        print (lista)

        if (registro in lista):
            return "<h1>Login efetuado com sucesso</h1>"
            # render_template("disciplinas.html")
        else:
            return "<h1>Login Mal sucedido</h1>"

        return "<h1>Login efetuado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

@app.route("/cadastroaluno", methods = ["POST", "GET"])
def hello():
    return render_template('index3.html')

@app.route("/cadastroprofessor", methods = ["POST", "GET"])
def vamos():
    return render_template('index4.html')

@app.route("/registroaluno", methods = ["POST", "GET"])
def registroaluno():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"

        #verificar se a variável user tem uma letra
        #maiúscula

        registro = user + " - " + senha 
        
        print (registro)

        arquivo = open("registro_aluno.txt","a")
        arquivo.writelines(registro)
        return "<h1>Cadastro realizado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

@app.route("/registroprofessor", methods = ["POST", "GET"])
def registroprofessor():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"

        #verificar se a variável user tem uma letra
        #maiúscula

        registro = user + " - " + senha 
        
        print (registro)

        arquivo = open("registro_professor.txt","a")
        arquivo.writelines(registro)

        return "<h1>Cadastro realizado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

app.run()