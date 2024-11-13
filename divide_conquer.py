from samba.dcerpc.dcerpc import empty

def summary_simple(arr):
    """
    Метод, возвращающий сумму чисел массива,
    использующий циклический подход.
    """
    total = 0               #базовый случай
    for x in arr:           #обход каждого элемента массива arr[]
        total += x          #добавление каждого элемента к базовому случаю.
    return total            #возврат сформированной суммы.

print("Возврат суммы элементов массива [1,2,3] = " + str(summary_simple([1, 2, 3])))

def summary_recursive(arr, i = 0, summary = 0):
    """
    Рекурсивный метод подсчета элементов в списке.
    """
    if i >= len(arr):         #Логика рекурсии
        return summary
    else:
        return summary_recursive(arr, i+1, summary+1)

print("Рекурсивно. Возврат количества элементов массива [1,2,3] = " + str(summary_recursive([5])))


def find_biggest(arr, i = 1, i_max = 0):
    """Функция поиска наибольшего числа в массиве"""
    if arr[i] > arr[i_max]:     #Логика поиска большего числа
        i_max = i

    if i >= len(arr)-1:         #Логика рекурсии
        return arr[i_max]
    else:
        return find_biggest(arr, i+1, i_max)

tested_array = [4,6,4,233,2,6,]
biggest_value = find_biggest(tested_array)
print("Рекурсивно. Поиск наибольшего числа в массиве: " + str(biggest_value))

