# class No:
#         def __init__(self, valor):
#             self.valor = valor
#             self.proximo = None

class FilaDoCaralho:

    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def inserir_valor(self):
         valor_desejado = int(input("Digite um valor: "))
         if self.inicio is None:
            self.inicio = self.fim = valor_desejado
         else:
            novo_no = valor_desejado
            self.fim = novo_no
            self.tamanho += 1

    def remover_valor(self):
        valor_remover = int(input("Digite um valor para remover: "))
        print(len(self.tamanho))

    def imprimir(self):
        
