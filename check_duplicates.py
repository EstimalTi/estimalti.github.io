# проверяет наличие дубликатов в массиве
def check_duplicates(lst):
    return len(set(lst)) != len(lst)


print(check_duplicates([1, 2, 3]))
