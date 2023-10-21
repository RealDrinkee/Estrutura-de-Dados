class Node():


    def __init__(self, nome, peso=0, pai=None, filho=None):
        self.peso = peso
        self.pai = pai
        self.filho = [] if filho is None else filho
        self.nome = nome
        self.raiz = pai is None
        self.folha = not self.filho #Não tem filho

class Tree(Node):

    def __init__(self, nome, antecessores=None, sucessores=None, folhas = []):
        self.nome = nome
        self.folhas = folhas
        self.antecessores = [] if antecessores is None else antecessores
        self.sucessores = [] if sucessores is None else sucessores

    def inserir_node(self):
        if node not in self.antecessores:
            self.antecessores.append(node)
        if self not in node.sucessores:
            node.sucessores.append(self)

    def remover_node(self):
        if node in self.antecessores:
            self.antecessores.remove(node)
        if self in node.sucessores:
            a.remover_node(b)
            self.node.sucessores.remove(self)

filho1 = Node("Gabriel", 10, "Foil", "foilzinho")
print(f"Nome: {filho1.nome}\nPeso: {filho1.peso}\nPai: {filho1.pai}\nFilho: {filho1.filho}\nRaiz: {filho1.raiz}\nFolha: {filho1.folha}\n")
filho2 = Tree("Gabriel", 10, "Foil", "foilzinho")
print(f"Nome: {filho2.nome}\nAntecessores: {filho2.antecessores}\nSucessores: {filho2.sucessores}\nFolhas: {filho2.folhas}")
