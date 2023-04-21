frase = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
l = len(frase)
for i in range(0,l):
    if frase[i] == 'n':
        print(i + 1)