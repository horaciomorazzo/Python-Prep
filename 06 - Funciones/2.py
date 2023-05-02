def primo(n):
    for i in range(2,n):
        a = True
        if n % 2 == 0:
            a = False
            break
        if n % i == 0:
            a = False
            break
    return a
lista = []
lista1 = []
entrada = input("Escribe algo: ")
while entrada != "":
    entrada_nro = int(entrada)
    lista.append(entrada_nro)
    entrada = input("Escribe algo: ")
primos = [i for i in lista if primo(i)]
print(primos)
