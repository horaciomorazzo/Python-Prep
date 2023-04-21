negativos = []
i = 1
while i < 16:
    negativos.append(- i)
    i += 1
print(negativos)
i = 1
while i < 16:
    if i % 2 == 0:
        print(negativos[i - 1])
    i = i + 1
