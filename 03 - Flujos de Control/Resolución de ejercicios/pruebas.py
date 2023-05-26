def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

for num in range(1, 31):
    if es_primo(num):
        print(num)