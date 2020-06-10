#bottom-up o programacion dinamica
#Un problema a partir de subproblemas ya resueltos. 

def fibo(numero):
    a = 1
    b = 1
    c = 0
    for i in range(1, numero-1):
        c = a + b
        a = b
        b = c
    return c

def fibo2(numero):
    a = 1
    b = 1
    c = 0
    for i in range(1, numero-1):
        a, b=b, a+b
    return b

def fibo_bottom_up(numero):
    fib_parcial =  [1,1,2]
    while len(fib_parcial)
        fib_parcial.append(fib_parcial[-1]+fib_parcial[-2])
        print(fib_parcial)
    return fib_parcial[numero-1]

f = fibo_bottom_up(5)
print(f)