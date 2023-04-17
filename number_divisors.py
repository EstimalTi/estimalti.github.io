n = int(input())
# находит все делители чисел от 0 до n
for i in range(1, n+1):
    print(i, '- ', end='')
    for k in range(1, n+1):
        if i % k == 0:
            print(k, end='')
            print(', ', end='')
    print()
