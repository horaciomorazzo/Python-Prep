negativos = []
i = 1
while i < 16:
    negativos.append(- i)
    i += 1
print(negativos)
for i in negativos:
    if i % 2 == 0:
        print(negativos[i])
    