#  Faça um código para gerar a sequência de Fibonacci até o n-ésimo elemento. Em seguida, faça um código para encontrar o valor nessa sequência que seja 
#'mais próximo' de um dado valor 'x'.

#     Avalie a complexidade dos dois códigos.
#     Considere n > 99

class Fibonacci:

    def __init__(self):
        self.n = 0
        self.x = 0

    def choose_n(self):
        self.n = int(input("Digite o n-ésimo elemento: "))
        return self.n
    
    def choose_x(self):
        self.x = int(input("Digite o valor de x: "))
        return self.x
    
    def fibonacci(self, n):
        fib = [0,1]
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib
    
    def find_closest(self, fib, x):
        closest = fib[0]
        for i in range(1,len(fib)):
            if abs(fib[i]-x) < abs(closest-x):
                closest = fib[i]
        return closest
    
    def main(self):
        self.choose_n()
        self.choose_x()
        fib = self.fibonacci(self.n)
        print(fib)
        print(f"valor mais próximo de {self.x}: {self.find_closest(fib, self.x)}")

fibonacci = Fibonacci()
fibonacci.main()