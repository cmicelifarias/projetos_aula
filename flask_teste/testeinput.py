#x = input("Qual a sua idade: \n")
#print ("Sua idade é: " + x)

disciplinas = [["calc1",4],["alg1", 5]]

print(disciplinas[0])
print(disciplinas[0][0])
print(disciplinas[0][1])
print(disciplinas[1])
print(disciplinas[1][0])
print(disciplinas[1][1])

class Estudante:

  #construtor da classe estudante
  def __init__(self, nome = "", dre =""):
    self.nome = nome 
    self.dre = dre
    self.disciplinas = [["calc1",4],["alg1", 4]]
    self.notas = [7, 8]
    #lista ou dicionario de disciplinas e notas
  
  # deve dizer se o aluno foi ou não aprovado em uma disciplina
  #deve retornar uma string
  def media(self,p1,p2,p3):
    if p1+p2 >= 14:
      return "aprovado direto"
    elif 10 <= p1+p2 < 14:
      return "prova final"
    else:
      return "reprovado direto"
  
  #coeficiente de rendimento acumulado
  # numero de credito * nota para cada disciplina; soma tudo 
  #e divide pelo total de créditos cursados
  def calcula_CRA(self):
    total_cred = 0
    #o range do comprimento de 2 é [0,1]
    # len calcula o comprimento do vetor nesse caso 2
    for i in range(len(self.disciplinas)):
        total_cred += self.disciplinas[i][1]
   
    print (total_cred)

    cra = 0
    #[0,1]
    for i in range(len(self.notas)):
        cra += (self.notas[i]* self.disciplinas[i][1])/total_cred

    return cra

    # total_cred = vou pegar a posiçao [1] somar os créditos
    #cra = 0
    # for i in len(self.notas):
    #  cra += i+cred_dessa_disciplina/total_cred -> 7*4/8 + 8*4/8

#instanciando a classe
a = Estudante()
b = Estudante()
#printando do método média com os atributos 
# o método retornou uma string
c = a.media(5,6,7)
d = b.media(7,8,9)
print (c)
print(d)
print (a.calcula_CRA())
print(b.calcula_CRA())