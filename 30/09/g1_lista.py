
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

    def len_tamanho(self):
        print(self.__tamanho)
        return self.__tamanho

    def inserir_lista(self):
        try:
            valor = int(input("Digite um valor: "))
            if self.__inicio is None and valor != int:
                # Se a lista estiver vazia, crie o primeiro nó
                self.__inicio = self.__fim = Node(valor)
                self.__posicao_lista += 1
            else:
                # Caso contrário, insira um novo nó no início
                novo_node = Node(valor)
                novo_node.proximo = self.__inicio
                self.__inicio = novo_node
            self.__tamanho += 1
        except ValueError:
            print("Digite um valor válido!")
            return valor, self.__tamanho
    
    def mostrar_lista(self):
        atual = self.__inicio
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


    def remover_dado_lista(self):
        self.mostrar_lista()
        valor_desejado = input("Digite o valor que deseja remover: ")

        if valor_desejado in self.__tamanho:
            self.__tamanho.remove(valor_desejado)
            print(f"Valor {valor_desejado} removido com sucesso!")
        else:
            print(f"Valor {valor_desejado} não encontrado na lista.")


        
class Node:
    def __init__(self, valor):
        self.valor = valor # Armazena o valor do nó atual
        self.proximo = None # Armazena o próximo nó da lista




class main():
    def __init__(self):
        self.__opcao = 0

    def get_opcao(self):
        return self.__opcao
    
    def set_opcao(self, opcao):
        self.__opcao = opcao

    def menu(self):
        while True:
            print("1 - Inserir valor\n2 - Mostrar tamanho\n3 - Mostrar lista e dados da lista\n4 - Remover dado da lista\n5 - Valor aleatório\n6 - Sair")
            self.__opcao = input("Escolha uma opção: ")
            try:
                if self.__opcao == "1":
                    minha_lista.inserir_lista()
                elif self.__opcao == "2":
                    minha_lista.len_tamanho()
                elif self.__opcao == "3":
                    minha_lista.mostrar_lista()
                    minha_lista.mostrar_dados_lista()
                elif self.__opcao == "4":
                    minha_lista.remover_dado_lista()
                elif self.__opcao == "5":
                    minha_lista.valor_aleatorio()
                elif self.__opcao == "6":
                    break
                else:
                    print("Digite uma opção válida!")
            except BaseException as error:
                print(f"Ocorreu um erro: {error}")


minha_lista = funcoes()
minha_lista.__init__()
main = main()
main.menu()
