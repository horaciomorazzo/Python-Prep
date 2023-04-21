lista = [1,2,5,7,8,10,13,14,15,17,20]
n = 1
while(n <= 20):
    if (not(n in lista)):
        lista.insert((n-1), n)
    n += 1
print(lista)
