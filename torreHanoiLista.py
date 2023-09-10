# Considere o jogo Torre de Hanói, de Édouard Lucas, com as regras
# abaixo:
#
# i. O objetivo do jogo é mover todos os discos do pino A para o pino
# C;
# ii. Só é possível mover um disco por vez;
# iii. Um disco maior não pode ser colocado sobre um disco menor.

class TorreHanoiLista:
    def __init__(self):
        self.__A = [1, 2, 3]
        self.__B = []
        self.__C = []

    def movimento(self):
        if self.__A:
            element = self.__A.pop(0)
            self.__C.insert(0, element)
            element = self.__A.pop(0)
            self.__B.insert(0, element)
            element = self.__C.pop(0)
            self.__B.insert(1, element)
            element = self.__A.pop(0)
            self.__C.insert(0, element)
            element = self.__B.pop(0)
            self.__A.insert(0, element)
            element = self.__B.pop(0)
            self.__C.insert(0, element)
            element = self.__A.pop(0)
            self.__C.insert(1, element)




obj = TorreHanoiLista()


obj.movimento()
print("A:", obj._TorreHanoiLista__A)
print("B:", obj._TorreHanoiLista__B)
print("C:", obj._TorreHanoiLista__C)
