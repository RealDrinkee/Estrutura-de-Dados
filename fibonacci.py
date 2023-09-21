#Faça um coidgo para que gerar a sequencia de fibonacci até o n em seguida, 
#faça um codigo para encontrar o valor nessa sequencia que seja o mais proximo de um dado valor 'x'
#Considere n> 99

n = 100
x = 24

def fibonacci(n):
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib

def find_closest(fib, x):
    closest = fib[0]
    for i in range(1,len(fib)):
        if abs(fib[i]-x) < abs(closest-x):
            closest = fib[i]
    return closest

fib = fibonacci(n)
print(fib)