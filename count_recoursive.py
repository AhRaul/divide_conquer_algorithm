def summary_recursive(arr, i = 0, summary = 0):
    """
    Рекурсивный метод подсчета элементов в списке.
    """
    if i >= len(arr):           #Базовый случай
        return summary
    else:                       #Рекурсивный случай
        return summary_recursive(arr, i+1, summary+1)

print("Рекурсивно. Возврат количества элементов массива [1,2,3] = "
      + str(summary_recursive([5])))