import queue

class FilaEncadeada:

    def __init__(self):
        self.fila = queue.Queue() # Criar uma instância de queue.Queue
 
    def adicionar_dado(self, valor_desejado):
        self.fila.put(valor_desejado)
        print(f"Dados adicionados com sucesso: {valor_desejado}")

    def ler_dados_da_lista(self):
        if self.fila.empty():
            print("Lista vazia")
        else:
            print("Lista:", list(self.fila.queue))

    def remover_dados_da_lista(self):
        if not self.fila.empty():
            valor_removido = self.fila.get()
            print(f"Dado removido com sucesso: {valor_removido}")
        else:
            print("A fila está vazia")

class MainMenu:
    def __init__(self):
        self.fila_encadeada = FilaEncadeada()

    def menu(self):
        while True:
            print("1 - Inserir valor\n2 - Remover valor\n3 - Imprimir\n4 - Sair")
            opcao = int(input("Digite uma opção: "))
            try:
                if opcao == 1:
                    valor_desejado = int(input("Digite um valor: "))
                    self.fila_encadeada.adicionar_dado(valor_desejado)
                elif opcao == 2:
                    self.fila_encadeada.remover_dados_da_lista()
                elif opcao == 3:
                    self.fila_encadeada.ler_dados_da_lista()
                elif opcao == 4:
                    break
                else:
                    print("Entrada inválida")
            except ValueError:
                print("Entrada inválida")

if __name__ == "__main__":
    MainMenu().menu()
