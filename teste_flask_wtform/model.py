#importa a biblioteca para manipulação do sgbd sqlite3
import sqlite3

# ou se conecta ao BD ou cria caso não haja BD
# um Banco de dados pode ter 1 ou mais tabelas
connection = sqlite3.connect("teste.db")

#método que cria a tabela 
#só precisa rodar uma vez
# o campo único de uma tabela é chamado de chave

def create():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE login (name TEXT, senha TEXT)")

#método para inserir na base de dados
# essa não é a forma segura de programar
def insere(nome, senha):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO login VALUES ('"+nome+"', '"+senha+"')")

#método para consultar se um dado nome está no banco
#essa não é a forma segura de programar
def consulta(nome):
    cursor = connection.cursor()
    rows = cursor.execute("SELECT "+ nome +" FROM login").fetchall()
    return rows