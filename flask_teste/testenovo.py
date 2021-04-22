class Pai:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Classe Pai")

class Filho(Pai):
    def berra(self):
        pass

class Filha(Pai):
    def __init__(self,a,b):
        # super chama o construtor da classe pai ou qq método
        #Pai.__init__(self,a,b)
        super().__init__(a,b)
        print("Classe filha")

a = Pai(1,2)

print(a.a)

b = Filha(1,2)

print(b.a)

c = Filho(1,2)

print(c.a)