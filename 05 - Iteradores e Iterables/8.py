lista = [0,1]
n = 1
while n < 31:
    n += 1
    f1 = lista[n - 1]
    f2 = lista[n - 2]
    f = f2 + f1
    lista.insert(n,f)
listaiterada = iter(lista)
print(sum(lista))
