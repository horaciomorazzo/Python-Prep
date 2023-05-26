def primo(n):
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
        