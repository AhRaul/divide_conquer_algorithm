def find_biggest(arr, i = 1, i_max = 0):
    """Функция поиска наибольшего числа в массиве"""
    if arr[i] > arr[i_max]:     #Логика поиска большего числа
        i_max = i

    if i >= len(arr)-1:         #Базовый случай(проверка каждого элемента массива)
        return arr[i_max]
    else:                       #Рекурсивный случай
        return find_biggest(arr, i+1, i_max)

tested_array = [4,6,4,233,2,6,]
biggest_value = find_biggest(tested_array)
print("Рекурсивно. Поиск наибольшего числа в массиве: " + str(biggest_value))
