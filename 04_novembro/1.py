#função fatorial

def fatorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(2, n+1):
            resultado *= i
        return resultado

def rfatorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * rfatorial(n-1)

for n in range(-7, 8):
    print(f"{n}! = {fatorial(n)}")

print(rfatorial(7))