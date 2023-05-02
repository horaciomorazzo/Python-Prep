lista = [2,2,4,5,6,2,13,13,1,1,4,8,8,8,8,8,5,5]
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


            
    










