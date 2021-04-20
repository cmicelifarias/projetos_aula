class Aluno:
    
    def __init__(self, user, senha):
        self.__user = user
        self.__senha = senha

    def salva(self):
        
        registro = self.__user + " - " +self.__senha
        arquivo = open("registro_aluno.txt","a")
        arquivo.writelines(registro)

    def getuser(self):

        return self.__user
    
    def getsenha(self):
        
        return self.__senha