#Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c='True'):  #Вывод функции
    print(a, b, c)


print_params()
print_params()
print_params()
print()


def print_params(a, b='строка', c='True',
                 d=None):  #Вывод функции с разным количеством аргументов, включая вызов без аргументов.
    if d is None:
        d = []
        d.append(a)
        print(d)
    print(a, b, c, d)


print_params(1)
print_params(2, 2)
print_params(3, 2, c='False')
print()
print()

#Распаковка параметров
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}


def print_params(a, b, c):
    print(a, b, c)


print_params(*values_list)  #распаковка списка
print_params(**values_dict)  #распаковка словаря
print()
print()

#Распаковка + отдельные параметры:
values_list_2 = [1, 'ctr']


def print_params(a, b):
    print(a, b)


print_params(*values_list_2, 42)
