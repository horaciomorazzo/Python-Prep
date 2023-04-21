lista = list('Hola Mundo. Esto es una practica del lenguaje de programación Python')
print(lista)
listaiterable = iter(lista)
for c in listaiterable:
    print(c)