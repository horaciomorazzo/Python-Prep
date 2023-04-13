def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = 2
r = " "
while r != "1":
    for num in range(2, a):
        if es_primo(num):
            print(num)
            r = input('Sigo?')
            a += 1


            




        
        



 