ciudades = ['Roma','Londres','San Petesburgo','Madrid','Montecarlo','Ibiza']
incluida = False
for i in range(0,6):
    if ciudades[i] == 'París':
        print('París está en la lista')
        incluida = True
        break
    
if incluida == False:
    print('París no está en la lista. Se agregará')
    ciudades.append('París')
    print('Lista completa:',ciudades)