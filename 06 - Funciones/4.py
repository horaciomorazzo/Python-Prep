#   def repetidos(lista,mm):
# lista contiene los números a clasificar
# Ingresar 'M' si desea el mas repetido
# Ingresar 'm' si desea el menos repetido
# Cualquier otro ingreso muestra nada
lista = [4,4,5,6,6,6,7,7,8]
mm = 'M'
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
minimo = min(lista2)
posicionmax = lista2.index(maximo)
posicionmin = lista2.index(minimo)
if mm == 'M':
    print('Máximo repetido:',lista1[posicionmax],'(',lista2[posicionmax],'veces )')
if mm == 'm':
    print(lista1[posicionmin],lista2[posicionmin])
print('Hasta la vista Baby!')

    
