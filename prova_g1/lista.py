class adicionar_dado_invalido(Exception):
    print("Entrada inválida")

class recebe_dados:
    def __init__(self, dado_atual):
        self.dado_atual = dado_atual
        self.proximo_dado = None

class lista_encadeada: 
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_dado(self):
        adicionar_valor = int(input("Digite um valor: "))
        novo_dado = recebe_dados(adicionar_valor)  # Criar uma instância de recebe_dados
        if self.inicio is None:
            self.inicio = self.fim = novo_dado  # Adicionar a instância à lista
            print(f"Dados adicionados com sucesso: {adicionar_valor}")
        else:
            self.fim.proximo_dado = novo_dado
            self.fim = novo_dado
            print(f"Dados adicionados com sucesso: {adicionar_valor}")
            return self.inicio, self.fim
        
    def ler_dados_da_lista(self):
        if self.inicio is None:
            print("Lista vazia")
            self.adicionar_dado()
        else:
            print("Lista:")
            atual = self.inicio
            while atual is not None:
                print(atual.dado_atual, end=" -> ")
                atual = atual.proximo_dado
            print("None")
        
    def remover_dados_da_lista(self):
        self.inicio = None
        self.fim = None
        print("Dados removidos com sucesso\n")
        print(f"Dados dentro da lista: {self.inicio, self.fim}")

class main_menu(lista_encadeada):
    def __init__(self):
        super().__init__()

    def menu(self):
        while True:
            print("1 - Inserir valor\n2 - Remover valor\n3 - Imprimir\n4 - Sair")
            opcao = int(input("Digite uma opção: "))
            try:
                if opcao == 1:
                    self.adicionar_dado()
                elif opcao == 2:
                    self.remover_dados_da_lista()
                elif opcao == 3:
                    self.ler_dados_da_lista()
                elif opcao == 4:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Opção inválida")

m = main_menu()
m.menu()
