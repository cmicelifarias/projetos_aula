from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm

app = Flask(__name__)

#opção de segurança
app.config.from_object(Config)

@app.route("/")
@app.route("/index")
def hello():
    return "<h1>Bem vindo ao começo de uma aplicação mais complexa</h1>"

'''
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
            #uma função de validação via banco de dados
            # e redirecionar para alguma outra página
        return redirect(url_for('/'))
    return render_template('login.html', title='Login', form=form)

app.run()