# Avalie a complexidade de um código para calcular a soma dos itens da lista 'a' q
# ue forem menores que o elemento da lista 'b', armazenando em uma lista 'c' o resultado da soma calculada, multiplicada pelo elemento de 'b'.
# Ex:
# a=[1,2,3,4,5,...,n]
# b=[5,6,7,8,9,...,n]
# c=[5.sum(a), 6.sum(a), 7.sum(a), ..., n.sum(a)]

#     n é o número de elementos
#     considere n > 30
import random

class Desafio:

    def __init__(self):
        self.a = []
        self.b = []
        self.c = []

    def primeira_lista(self):
        primeira_lista = int(input("Digite o tamanho da primeira lista: "))
        for index in range(primeira_lista):
            self.a.append(random.randint(0, primeira_lista))

    def segunda_lista(self):
        segunda_lista = int(input("Digite o tamanho da segunda lista: "))
        for index in range(segunda_lista):
            self.b.append(random.randint(0, segunda_lista))

    def calcular_soma(self):
        if len(self.a) != len(self.b):
            print("As listas precisam ter o mesmo tamanho!")
            return
        
        for index in range(len(self.a)):
            if self.a[index] < self.b[index]:
                self.c.append(self.a[index] * self.b[index])

                

        print("Lista 'a':", self.a)
        print("Lista 'b':", self.b)
        print("Lista 'c': multiplicada:", self.c)


desafio = Desafio()
desafio.primeira_lista()
desafio.segunda_lista()
desafio.calcular_soma()

