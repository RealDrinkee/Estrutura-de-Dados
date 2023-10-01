class funcoes():

    def __init__(self):
        self.__tamanho = 0
        self.__inicio = None
        self.__fim = None
        self.__posicao_lista = 0


    def get_tamanho(self):
        return self.__tamanho
    
    def get_init(self):
        return self.__inicio
    
    def get_fim(self):
        return self.__fim
    
    def get_posicao_lista(self):
        return self.__posicao_lista
    

    def inserir_valor_lista(self):
        valor = input("Digite um valor: ")
        posicao_lista = int(input("Digite a posição que deseja adicionar: "))
        insert = {
            "valor": valor,
            "posicao_lista": posicao_lista
        }

        if self.__inicio is None:
            self.__inicio = self.__fim = insert
            self.__posicao_lista += 1

        else:
            novo_node = insert
            novo_node.proximo = self.__inicio
            self.__inicio = novo_node
            self.__posicao_lista += 1

    def mostrar_lista(self):
        atual = self.__inicio
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def mostrar_dados_lista(self):
        atual = self.__inicio
        print(f"Tamanho da lista: {self.__tamanho}")
        print(len(atual.valor))

class Node:
    def __init__(self, valor):
        self.valor = valor # Armazena o valor do nó atual
        self.proximo = None # Armazena o próximo nó da lista

# Exemplo de uso:
minha_lista = funcoes()
minha_lista.__init__()
minha_lista.inserir_valor_lista()
minha_lista.mostrar_lista()
minha_lista.mostrar_dados_lista()
