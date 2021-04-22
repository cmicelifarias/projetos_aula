from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index2.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]
        if user == "buda" and senha == "buda":
            return "<h1>login com sucesso</h1>"
        else:
            return "Login mal sucedido"
     
app.run()