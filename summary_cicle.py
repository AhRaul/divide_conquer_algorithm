def summary_simple(arr):
    """
    Метод, возвращающий сумму чисел массива,
    использующий циклический подход.
    """
    total = 0               #базовый случай (нулевое значение взято как возможный минимум)
    for x in arr:           #обход каждого элемента массива arr[]
        total += x          #добавление каждого элемента к базовому случаю.
    return total            #возврат сформированной суммы.

print("Возврат суммы элементов массива [1,2,3] = " + str(summary_simple([1, 2, 3])))