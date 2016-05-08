def fibonnaci (num):
    fibo = []
    a = 1
    b = 0
    c = 1
    for i in range(0,num):
        fibo.append(c)
        c = a + b
        b = a
        a = c
    return fibo

print(fibonnaci(10))