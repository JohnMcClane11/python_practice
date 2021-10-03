#получаем входные данные
numbers = input('Введите через пробел целые числа:\t').split()
any_number = int(input('Введите любое число:\t'))
print('---------------')
#делаем список чисел
numbers_list = list(int(i) for i in numbers)
#сортируем список
def merge_sort(list_):
    if len(list_) < 2:
        return list_[:]
    else:
        middle = len(list_) // 2
        left = merge_sort(list_[:middle])
        right = merge_sort(list_[middle:])
        return merge(left, right)
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result
numbers_list = merge_sort(numbers_list)
print(f'Список чисел, отсортированный по возрастанию: {numbers_list}')
print('---------------')
#устанавливаем номер позиции элемента, который < any_number или >= any_number
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за границы списка. Введите другое число.'

if not binary_search(numbers_list, any_number, 0, len(numbers_list)):
    bottom_number = min(numbers_list, key=lambda x: (abs(x - any_number), x))
    indx = numbers_list.index(bottom_number)
    max_indx = indx + 1
    min_indx = indx - 1
    if bottom_number < any_number:
        print(f'''В списке отсутствует заданное число!
Ближайшее число из списка меньше заданного числа:\t{bottom_number} с индексом {indx}
Ближайшее число из списка больше заданного числа:\t{numbers_list[max_indx]} с индексом {max_indx}''')
        print('---------------')
    elif bottom_number > any_number:
        print(f'''В списке отсутствует заданное число!
Ближайшее число из списка больше заданного числа:\t{bottom_number} с индексом {numbers_list.index(bottom_number)}
В списке нет числа меньше, чем заданное число''')
        print('---------------')
    elif min_indx < 0:
        print(f'''В списке отсутствует заданное число!
Ближайшее число из списка больше заданного числа:\t{bottom_number} с индексом {numbers_list.index(bottom_number)}
В списке отсутствует число, которое меньше заданного''')
        print('---------------')
    elif numbers_list.index(bottom_number) == 0:
        print(f'Индекс заданного числа:\t{numbers_list.index(bottom_number)}')
        print('---------------')
else:
    print(f'Индекс заданного числа:\n{binary_search(numbers_list, any_number, 0, len(numbers_list))}')
    print('---------------')