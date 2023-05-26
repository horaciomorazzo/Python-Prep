class Herramientas:
    #global a
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def esprimo(self):
        for i in self.lista:
            self.primo(i)
    
    def primo(self, n):
        a = True
        for i in range(2,n):
            if n % i == 0:
                a = False
                break
        if (a == True) and (n != 1):
            print(n,'es número primo')
        else:
            print(n,'no es número primo')

    def modal(self):
        #lista = input('Ingrese una lista de números')
        self.lista.sort()
        nuevalista = []
        indice = 0
        while indice != (len(self.lista) - 1):
                if self.lista[indice + 1] != self.lista[indice]:
                    nuevalista.append(self.lista[indice])
                indice += 1
                #print(indice)
        nuevalista.append(self.lista[indice])
        lista1 = []
        lista2 = []
        for i in range (0,len(nuevalista)):
            a = nuevalista[i]
            b = self.lista.count(a)
            if b > 1:
                lista1.append(a)
                lista2.append(b)
        if lista2 == []:
            print('No existe el valor modal para la lista ingresada')
        else:
            maximo = max(lista2)
            i = 0
            while lista2[i] != maximo:
                i += 1
            print(lista1[i])

    def conversion(self, umedida, r):
        for i in self.lista:
            self.conversion1(i,umedida,r)

    
    def conversion1(self, valor, umedida, r):
        valor1 = float(valor)
        if umedida == 'K':
            if r == 'C':
                print(valor1,'°K equivalen a',valor1 - 273.15,'°C')
            if r == 'F':
                print(valor1,'°F equivalen a',(((valor1 - 273.15) * 9 / 5)) + 32,'°F')
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
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de',i,'es',self.calcular_factorial1(i))
    
    def calcular_factorial1(self,num):
        f = 1
        for i in range(1, num + 1):
            f = f * i
        return f
    
            