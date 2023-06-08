def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
r = '2'
num = 1
while r != "1":
    num += 1
    if es_primo(num):
        print(num)
        r = input('Sigo?. Ingrese 1 para finalizar')
print('Hasta la vista!')



            




        
        



 