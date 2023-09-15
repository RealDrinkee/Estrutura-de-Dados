class TorreHanoiPilhas:
    def __init__(self):
        self.pinoA = [1, 2, 3]
        self.pinoB = []
        self.pinoC = []
        self.movimentos = 0

    def __str__(self):
        return f'Pino A: {self.pinoA}\nPino B: {self.pinoB}\nPino C: {self.pinoC}'

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

    def funcao_pinoA(self):
            para_qual = str(input("Para qual pino deseja movimentar? (B ou C): ")).upper()
            if para_qual == 'B':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoB.append(self.pinoA.pop(0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoB.append(self.pinoA.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoB.append(self.pinoA.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")
            elif para_qual == 'C':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoC.append(self.pinoA.pop(0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoC.append(self.pinoA.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoC.append(self.pinoA.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")    
            else:
                print("Movimento inválido!")    

    def funcao_pinoB(self):
            para_qual = str(input("Para qual pino deseja movimentar? (A ou C): ")).upper()
            if para_qual == 'A':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoA.append(self.pinoB.pop(0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoA.append(self.pinoB.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoA.append(self.pinoB.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")
            elif para_qual == 'C':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoC.append(self.pinoB.pop(0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoC.append(self.pinoB.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoC.append(self.pinoB.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")

    def funcao_pinoC(self):
            para_qual = str(input("Para qual pino deseja movimentar? (A ou B): ")).upper()
            if para_qual == 'A':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoA.append(self.pinoC.pop(0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoA.append(self.pinoC.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoA.append(self.pinoC.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")
            elif para_qual == 'B':
                escolher_pino = int(input("Qual do pino deseja movimentar? (1, 2 ou 3): "))
                if escolher_pino == 1:
                    self.pinoB.append(self.pinoC.pop(-0))
                    self.movimentos += 1
                elif escolher_pino == 2:
                    self.pinoB.append(self.pinoC.pop(1))
                    self.movimentos += 1
                elif escolher_pino == 3:
                    self.pinoB.append(self.pinoC.pop(2))
                    self.movimentos += 1
                else:
                    print("Movimento inválido!")


if __name__ == '__main__':
    jogo = TorreHanoiPilhas()
    jogo.main()
