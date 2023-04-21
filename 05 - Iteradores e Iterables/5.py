negativos = []
i = 1
while i < 16:
    negativos.append(- i)
    i += 1
print(negativos)
primeros = iter(negativos)
for i, c in enumerate(primeros):
    if i < 4:
        print(i,c)