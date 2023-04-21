lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lisiter = iter(lis)
n = len(lis)
i = 0
num = 0
while i < n:
    i += 1
    a = next(lisiter)
    if type(a) == list:
        num = num + len(a)
    else:
        num = num + 1
print('La cantidad de elementos es: ',num)
