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

def binary_find_recursive(arr, finding_value, left_index = '', right_index = ''):
    """Бинарный поиск с использованием рекурсии"""
    if left_index == '':
        left_index = 0                 #Индекс, первого значения массива
    if right_index == '':
        right_index = len(arr) - 1     #Индекс, последнего значения массива
    current_index = (right_index + left_index) // 2    #индекс, Рассматриваемого среднего значения,
                                                         # в рассматриваемом диапазоне.
    if finding_value > arr[current_index]:  #Проверка левой части.
        left_index = current_index + 1              #Если да, то сброс левой части массива
    elif finding_value < arr[current_index]:                                #Проверка правой части.
        right_index = current_index - 1             #Если да, то сброс правой части массива
    elif finding_value == arr[current_index]:       # Если значение в массиве найдено, вернуть его индекс
        return current_index

    if left_index > right_index:  # Если все возможные значения отброшены, конец поиска.
        return None                     #Базовый случай
    else:                          # Если значения еще остались
        return binary_find_recursive(arr, finding_value, left_index, right_index)  # запуск рекурсии

tested_sorted_array = [2,3,6,9,22,30,99]
finding_value = 6
result_finding_index = binary_find_recursive(tested_sorted_array, finding_value)
print("Тест рекурсивного метода бинарного поиска. "
      "Индекс искомого значения '" + str(finding_value) + "' равен: " + str(result_finding_index))