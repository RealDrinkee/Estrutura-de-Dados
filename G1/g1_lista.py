# Implementar uma lista simplesmente encadeada em python
# Requisitos:
# Não usar [ ] (significa que não deve ser utilizada a estrutura padrão de lista do python)
# Não usar [ ] dentro de outra estrutura (significa que não deve ser utilizada a estrutura padrão de lista do python)
# Operações mínimas para a implementação de lista:
# Inicialização da lista
# Inserção de itens (em qualquer posição)
# Remoção de itens (em qualquer posição)
# Acesso a item aleatório (acesso ao item a partir do seu índice, retornando o valor e acesso a partir do valor, retornando o índice)
# Retornar o tamanho da lista
# Iteração (retornar os itens da lista, um a um, a partir do primeiro)
# ** Somente neste caso específico é permitido retornar uma listpythona padrão do python com os itens **
# GOLDEN FEATURE: implementar utilizando classes do python

class no():
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class lista():

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_valor(self):
        valor = int(input("Digite um valor: "))
        posicao_lista = int(input("Digite a posição que deseja inserir o valor: "))
        if posicao_lista == 0:
            self.inicio = self.fim = no(valor)
        else:
            novo_no = no(valor)
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            self.tamanho += 1

    def mostrar_lista(self):
        atual = self.inicio
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def remover_dado_lista(self):
        self.mostrar_lista()
        valor_desejado = input("Digite o valor que deseja remover: ")

        if valor_desejado in self.tamanho:
            self.tamanho.remove(valor_desejado)
            print(f"Valor {valor_desejado} removido com sucesso!")
        else:
            print(f"Valor {valor_desejado} não encontrado na lista.")


lista = lista()
lista.inserir_valor()
lista.mostrar_lista()
lista.remover_dado_lista()



