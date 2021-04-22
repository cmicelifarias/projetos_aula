#desenvolvimento backend

from flask import Flask
from flask import render_template

#import numpy as np

'''
comentario de varias linhas
buda = 5
print(buda)
buda = "Oi"
print(buda)
'''

# a variavel buda esta recebendo o conteudo da pagina
buda = Flask(__name__)

#eh um decorador
@buda.route("/")
def hello():
    return render_template('index.html')

@buda.route("/teste")
def hello2():
    return "<h1>Essa é outra página</h1>"

@buda.route("/hello/")
@buda.route('/hello/<name>')
def hello3(name=None):
    return render_template("hello.html",name=name )

#essa é a função que coloca as coisas para rodarem
buda.run()