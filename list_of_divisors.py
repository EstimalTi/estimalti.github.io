# создает список из делителей числа
n = int(input())
catalog = []

for i in range(1, n+1):
    if n % i == 0:
        catalog.append(i)
print(catalog)
