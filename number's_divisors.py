# находит все делители чисел от 1 до n
n = int(input())

for i in range(1, n + 1):
    print(i, end='')
    print(': ', end='')
    for k in range(1, n + 1):
        if i % k == 0:
            print(k, end='')
            print('  ', end='')
    print()
