import pandas as pd

class G1Listas:

    def __init__(self):
        self.__minha_sequencia = pd.Series()

    def get_lista(self):
        return self.__minha_sequencia
    
    def inserir_lista(self):
        adicionar_item = input("Digite o item que deseja adicionar: ")
        posicao_lista = int(input("Digite a posição que deseja adicionar: "))
        self.__minha_sequencia.at[posicao_lista] = adicionar_item 
        print(f"Posição: {posicao_lista} - Item: {adicionar_item}")
        adicionar_mais = input("Deseja adicionar mais itens? (S/N): ").upper()
        if adicionar_mais == 'S':
            self.inserir_lista()
        else:
            print("Fim da inserção de itens!")
        
    def remover_lista(self):
        while True:
            opcao = int(input("1 - Remover tudo\n2 - Remover por posição\n3 - Remover por valor\n4 - Voltar ao menu principal\nEscolha uma opção: "))
            try:
                if opcao == 1:
                    self.__minha_sequencia = pd.Series()
                    print(self.__minha_sequencia)
                elif opcao == 2:
                    posicao_remover = int(input("Digite a posição que deseja remover: "))
                    self.__minha_sequencia.drop(posicao_remover, inplace=True) #Drop usado para remover elementos por indice
                    print(self.__minha_sequencia)
                elif opcao == 3:
                    valor_remover = input("Digite o valor que deseja remover: ")
                    self.__minha_sequencia = self.__minha_sequencia[self.__minha_sequencia != valor_remover]
                    print(f"Lista: {self.__minha_sequencia}")
                elif opcao == 4:
                    break
                else:
                    print("Opção inválida!")
            except BaseException as error:
                print(f"Ocorreu um erro: {error}")

    def acessar_valor_aleatorio(self):
        valor_aleatorio = self.__minha_sequencia.sample().values[0] #amostragem aleatória dos dados na série
        print(f"Valor aleatório: {valor_aleatorio}")


    def retornar_tamanho_lista(self):
        print(f"Tamanho da lista: {len(self.__minha_sequencia)}")

    def iterar_lista(self):
        for item in self.__minha_sequencia:
            yield item  # Utilize um gerador para retornar os itens um a um

    def main(self):
        while True:
            print("Sequência de listas")
            print("1 - Inserir itens\n2 - Remover itens\n3 - Acessar valor aleatório\n4 - Retornar tamanho da lista\n5 - Iterar lista\n6 - Sair")
            opcao = int(input("Escolha uma opção: "))
            try:
                if opcao == 1:
                    self.inserir_lista()
                elif opcao == 2:
                    self.remover_lista()
                elif opcao == 3:
                    self.acessar_valor_aleatorio()
                elif opcao == 4:
                    self.retornar_tamanho_lista()
                elif opcao == 5:
                    for item in self.iterar_lista():
                        print(f"Item: {item}")
                elif opcao == 6:
                    break
                else:
                    print("Opção inválida!")
            except BaseException as error:
                print(f"Ocorreu um erro: {error}")

g1 = G1Listas()
g1.main()
