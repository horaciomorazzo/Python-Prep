    
def conversion(valor,umedida,r):
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


