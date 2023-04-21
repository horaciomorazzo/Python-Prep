lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lisiter = iter(lis)
lis1 = lis
n = len(lis)
i = 0
ab = 0
num = 0
while i < n:
    i += 1
    a = next(lisiter)
    if type(a) == list:
        num = num + len(a)
    else:
        ab = ab + 1
        lista = list(a)
        lis.append(lista) 
del lis[1]
del lis[1]
print(lis)
