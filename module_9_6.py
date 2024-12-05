from itertools import combinations # из библиотеки вызываем функцию

def all_variants(text):             # создаем функцию генератор
    for i in range(1, len(text)+1): # перебираем список из элементов включительно
        lis = []                    # создаем список
        b = combinations(text, i)   # создаем комбинации из элементов
        lis.extend(b)               # добавляем комбинации в список
        for j in lis:
            j = list(j)             # создаем список из наших элементов
            yield (''.join(j))      # возвращаем данные в генератор с объединением списка в одну строку


a = all_variants("abc")
for i in a:
    print(i)