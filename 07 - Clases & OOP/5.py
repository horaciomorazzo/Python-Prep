class Herramientas:
    def __init__(self):
        pass

    def primo(self, n):
        for i in range(2,n):
            a = True
            if n % 2 == 0:
                a = False
                break
            if n % i == 0:
                a = False
                break
        if a == True:
            print(n,'es número primo')
        else:
            print(n,'no es número primo')

    def modal(self, lista):
        #lista = input('Ingrese una lista de números')
        lista.sort()
        nuevalista = []
        indice = 0
        while indice != (len(lista) - 1):
                if lista[indice + 1] != lista[indice]:
                    nuevalista.append(lista[indice])
                indice += 1
                #print(indice)
        nuevalista.append(lista[indice])
        lista1 = []
        lista2 = []
        for i in range (0,len(nuevalista)):
            a = nuevalista[i]
            b = lista.count(a)
            if b > 1:
                lista1.append(a)
                lista2.append(b)
        maximo = max(lista2)
        i = 0
        while lista2[i] != maximo:
            i += 1
        print(lista1[i])

    def conversion(self,valor,umedida,r):
        valor1 = float(valor)
        if umedida == 'K':
            if r == 'C':
                print('Equivalen a',valor1 - 273.15,'°C')
            if r == 'F':
                print('Equivalen a',(((valor1 - 273.15) * 9 / 5)) + 32,'°F')
        if umedida == 'C':
            if r == 'K':
                print('Equivalen a',valor1 + 273.15,'°K')
            if r == 'F':
                print('Equivalen a',(valor1 * 9 / 5 + 32),'°F')
        if umedida == 'F':
            if r == 'C':
                print('Equivalen a',(valor1 - 32) * 5 / 9,'°C')
            if r == 'K':
                print('Equivalen a',((valor1 + 273.15)) * 9 / 5 + 32,'°K')

    # Ingresando número negativo se convierte a positivo.
    # Los no enteros se convierten a la parte entera.
    
    def calcular_factorial(self,num):
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial
    
            