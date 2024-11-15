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
        return None                     #Базовый случай(минимальный возможный обьем проверяемого материала сводится к 1 элементу)
    else:                          # Если значения еще остались
        return binary_find_recursive(arr, finding_value, left_index, right_index)  # запуск рекурсии

tested_sorted_array = [2,3,6,9,22,30,99]
finding_value = 6
result_finding_index = binary_find_recursive(tested_sorted_array, finding_value)
print("Тест рекурсивного метода бинарного поиска. "
      "Индекс искомого значения '" + str(finding_value) + "' равен: " + str(result_finding_index))
