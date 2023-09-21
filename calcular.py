class Calcular:

    def __init__(self):
        self.__a = []
        self.__b = []

    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def gerar_lista_a(self):
        n = int(input("Digite o tamanho da lista A: "))
        for i in range(n):
            self.__a.append(i+1)
        print(self.__a)

    def gerar_lista_b(self):
        n = int(input("Digite o tamanho da lista B: "))
        for i in range(n):
            self.__b.append(i+1)
        print(self.__b)

    def calcular_soma_adjacentes(self, target):
        if target in self.__a:
            index = self.__a.index(target)
            if index > 0:
                left_neighbor = self.__b[index - 1]
            else:
                left_neighbor = 0
            if index < len(self.__a) - 1:
                right_neighbor = self.__b[index + 1]
            else:
                right_neighbor = 0
            result = target * (left_neighbor + right_neighbor)
            return result
        else:
            return None

    def calcular_para_todos(self):
        resultados = {}
        for numero in self.__a:
            resultado = self.calcular_soma_adjacentes(numero)
            if resultado is not None:
                resultados[numero] = resultado
        return resultados

    def main(self):
        self.gerar_lista_a()
        self.gerar_lista_b()
        resultados = self.calcular_para_todos()
        for numero, resultado in resultados.items():
            print(f"Para o número {numero}: Resultado = {resultado}")

if __name__ == "__main__":
    calcular = Calcular()
    calcular.main()
