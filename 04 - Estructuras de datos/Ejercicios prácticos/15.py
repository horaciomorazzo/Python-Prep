ciudades = ['Roma','Londres','París','Madrid','Montecarlo','Ibiza']
print (ciudades * 4)
# opcional del profe
# cuántas veces se repite cada nombre
repetidos = ['Roma','Roma','Salzburgo','Salzburgo','Salzburgo','Salzburgo','Viena','París','Azul','Azul','Olavarría']
repetidos.sort()
total = len(repetidos)
print(total)
cont = 1
cont1 = 0
for i in range (0,total):
    a = repetidos[i]
    if i < (total - 1):
        b = repetidos[i + 1]
        if a == b:
            cont = cont + 1
        if a != b:
            print(repetidos[i],cont)
            cont = 1            
    if i == total - 1:
        b = repetidos[i - 1]
        if a == b:
            print(repetidos[i],cont)
        if a != b:
            print(repetidos[i],'1')

    
   
    
       




            
    




