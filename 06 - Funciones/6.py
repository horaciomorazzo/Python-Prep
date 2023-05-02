def conversion(valor,umedida,r):
    valor1 = float(valor)
    if umedida == 'K':
        if r == 'C':
            print(valor1,'°K equivalen a',valor1 - 273.15,'°C')
        if r == 'F':
            print(valor1,'°K Equivalen a',(((valor1 - 273.15) * 9 / 5)) + 32,'°F')
    if umedida == 'C':
        if r == 'K':
            print(valor1,'°C Equivalen a',valor1 + 273.15,'°K')
        if r == 'F':
            print(valor1,'°C Equivalen a',(valor1 * 9 / 5 + 32),'°F')
    if umedida == 'F':
        if r == 'C':
            print(valor1,'°F Equivalen a',(valor1 - 32) * 5 / 9,'°C')
        if r == 'K':
            print(valor1,'°F Equivalen a',((valor1 + 273.15)) * 9 / 5 + 32,'°K')
# --------------------------------------------------------------------
lista = ['C','F','K','F','K','C','K','C','F']
for a in range(0,9,3):
    for b in range(1,3):
        conversion(1,lista[a],lista[a + b])
    

        

