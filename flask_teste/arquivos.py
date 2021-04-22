#arquivo = open("contatos.txt", "a")
#arquivo.write("Olá, mundo!")


''' comentario de multiplas linhas
em c comentario eh //
em python eh #

arquivo = open("contatos.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

print (frases)
arquivo.writelines(frases)

'''
arquivo = open("contatos.txt", "r")

print(arquivo.readline(3))

arquivo = open("contatos.txt", "r")

print(arquivo.readlines())
