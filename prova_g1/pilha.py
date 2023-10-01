class No:
    def __init__(self, valor):
        self.valor = valor # Valor do nó atual
        self.proximo = None # Próximo nó da pilha

class Pilha:

    def __init__(self):
        self.tamanho = 0
        self.topo = None

    def push(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def pop(self):
        if self.topo is None:
            print("A pilha está vazia")
            return None
        valor_removido = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor_removido

    def tamanho_pilha(self):
        return self.tamanho

    def imprimir(self):
        if self.topo is None:
            print("A pilha está vazia")
        else:
            atual = self.topo
            while atual is not None:
                print(atual.valor)
                atual = atual.proximo

    def menu(self):
        while True:
            print("1 - Inserir valor\n2 - Remover valor\n3 - Imprimir\n4 - Tamanho da pilha\n5 - Sair")
            opcao = int(input("Digite uma opção: "))
            try:
                if opcao == 1:
                    valor = int(input("Digite um valor: "))
                    self.push(valor)
                elif opcao == 2:
                    valor_removido = self.pop()
                    if valor_removido is not None:
                        print(f"Valor removido: {valor_removido}")
                elif opcao == 3:
                    self.imprimir()
                elif opcao == 4:
                    print(f"Tamanho da pilha: {self.tamanho_pilha()}")
                elif opcao == 5:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Opção inválida")

p = Pilha()
p.menu()
