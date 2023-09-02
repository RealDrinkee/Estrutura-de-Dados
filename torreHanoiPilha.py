# Fazer uma torre de Hanoi com Pilhas

class Pilha():

    def __init__(self):
        self.A = [3, 2 , 1]
        self.B = []
        self.C = []


    def movimento(self, origem, destino):
        if origem == "A":
            if destino == "B":
                self.B.append(self.A.pop())
            elif destino == "C":
                self.C.append(self.A.pop())
        elif origem == "B":
            if destino == "A":
                self.A.append(self.B.pop())
            elif destino == "C":
                self.C.append(self.B.pop())
        elif origem == "C":
            if destino == "A":
                self.A.append(self.C.pop())
            elif destino == "B":
                self.B.append(self.C.pop())

    def imprimir(self):
        print(self.A)
        print(self.B)
        print(self.C)
        print("")

    def resolver(self, n, origem, destino, auxiliar):
        if n > 0:
            self.resolver(n-1, origem, auxiliar, destino)
            self.movimento(origem, destino)
            self.imprimir()
            self.resolver(n-1, auxiliar, destino, origem)

pilha = Pilha()
pilha.imprimir()
pilha.resolver(3, "A", "C", "B")
