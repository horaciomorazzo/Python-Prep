negativos = []
i = 1
while i < 16:
    negativos.append(- i)
    i += 1
print(negativos)
primeros = iter(negativos)
for i in range (1,4):
    print(next(primeros))
