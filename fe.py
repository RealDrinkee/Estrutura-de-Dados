class node():
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class funcoes():

    def __init__(self):
        self.lista_do_caralh4 = {
            "tamanho": 0,
            "inicio": None,
            "fim": None,
            "posicao_lista": 0
        }


    def adicionar_valor(self):
        valor = int(input("Valor desejado: "))

        if self.lista_do_caralh4.get("inicio") is None:
            self.lista_do_caralh4.put("inicio", node(valor))
            self.lista_do_caralh4.put("fim", node(valor))
            self.lista_do_caralh4.put("posicao_lista", 1)
        else:
            novo_node = node(valor)
            novo_node.proximo = self.lista_do_caralh4.get("inicio")
            self.lista_do_caralh4.put("inicio", novo_node)
            self.lista_do_caralh4.put("posicao_lista", self.lista_do_caralh4.get("posicao_lista") + 1)

        self.lista_do_caralh4.put("tamanho", self.lista_do_caralh4.get("tamanho") + 1)


class menu():

    def __init__(self):
        self.opcao = 0

    def menu(self):
        print("1 - Adicionar valor")
        print("2 - Remover valor")
        print("3 - Mostrar lista")
        print("4 - Sair")
        self.opcao = int(input("Escolha uma opção: "))

        if self.opcao == 1:
            funcoes.adicionar_valor()
        elif self.opcao == 2:
            pass
        elif self.opcao == 3:
            pass
        elif self.opcao == 4:
            pass
funcoes = funcoes()
menu = menu()
menu.menu()


    