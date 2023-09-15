from collections import deque

class TorreHanoiPilhas:
    def __init__(self):
        self.pinoA = deque([3,2,1])
        self.pinoB = deque()
        self.pinoC = deque()
        self.movimentos = 0

    def __str__(self):
        return f'Pino A: {list(self.pinoA)}\nPino B: {list(self.pinoB)}\nPino C: {list(self.pinoC)}'

    def menu(self):
        print(self)
        print("1 - Movimentar pino A\n2 - Movimentar pino B\n3 - Movimentar pino C\n4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def main(self):
        while True:
            opcao = self.menu()
            try:
                if opcao == 1:
                    self.funcao_pinoA()
                elif opcao == 2:
                    self.funcao_pinoB()
                elif opcao == 3:
                    self.funcao_pinoC()
                elif opcao == 4:
                    break
                else:
                    print("Opção inválida!")
            except Exception as error:
                print(f"Ocorreu um erro: {error}")

    def movimentar(self, origem, destino):
        if not origem:
            print("Movimento inválido! Pino de origem vazio.")
            return
        if not destino or origem[-1] < destino[-1]:
            disco = origem.pop()
            destino.append(disco)
            self.movimentos += 1
        else:
            print("Movimento inválido! Disco maior não pode ser colocado sobre um menor.")

    def funcao_pinoA(self):
        para_qual = str(input("Para qual pino deseja movimentar? (B ou C): ")).upper()
        if para_qual == 'B':
            self.movimentar(self.pinoA, self.pinoB)
        elif para_qual == 'C':
            self.movimentar(self.pinoA, self.pinoC)
        else:
            print("Movimento inválido!")

    def funcao_pinoB(self):
        para_qual = str(input("Para qual pino deseja movimentar? (A ou C): ")).upper()
        if para_qual == 'A':
            self.movimentar(self.pinoB, self.pinoA)
        elif para_qual == 'C':
            self.movimentar(self.pinoB, self.pinoC)
        else:
            print("Movimento inválido!")

    def funcao_pinoC(self):
        para_qual = str(input("Para qual pino deseja movimentar? (A ou B): ")).upper()
        if para_qual == 'A':
            self.movimentar(self.pinoC, self.pinoA)
        elif para_qual == 'B':
            self.movimentar(self.pinoC, self.pinoB)
        else:
            print("Movimento inválido!")

if __name__ == '__main__':
    jogo = TorreHanoiPilhas()
    jogo.main()
