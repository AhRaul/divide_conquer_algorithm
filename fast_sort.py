def quicksort(array):
    """Быстрая сортировка"""
    if len(array) < 2:      #Базовый случай.
        return array        #Возвращается отсортированный массив,
                                # 1 элемент не надо сортировать.
    else:                   #Рекурсивный случай
        pivot = array[0]        #Первый элемент массива, выбран как опорный элемент, слево от которого
                                    # будут меньшие, чем он, элементы массива, а справа, большие.

        #less = [i for i in array[1:] if i <= pivot]      #Тут закомментирован сокращенный код формирования массива,
                                                            #который в развернутом виде представлен ниже.
        less = []                   #Инициализирован пустой Подмассив для всех элементов, меньших опорного.
        for i in array[1:]:     #Начинаем с 1 элемента, т.к. нулевой уже используется, как опорный.
            if i <= pivot:      #Если рассматриваемый элемент меньше или равен опорного.
            #Если написать вместо '<=' просто '<', то массив сформируется, упуская повторяющиеся элементы.
                less.append(i)      #Заполняем Подмассив всеми элементами, меньших опорного.

        #greater = [i for i in array[1:] if i > pivot]    #Тут закомментирован сокращенный код формирования массива,
                                                            #который в развернутом виде представлен ниже.
        greater = []                #Инициализирован пустой Подмассив всех элементов, больших опорного
        for i in array[1:]:     #Начинаем с 1 элемента, т.к. нулевой уже используется, как опорный.
            if i > pivot:      #Если рассматриваемый элемент больше опорного.
                greater.append(i)       #Заполняем Подмассив всеми элементами, больших опорного.

        #Предыдущие for можно объединить, для однократного обхода массива, вместо двукратного.
            # Но, для наглядности, они разделены, в учебных целях.

        return quicksort(less) + [pivot] + quicksort(greater)   #рекурсия, обратная сборка массива,
                                                                # из меньшей, опорного, и большей частей.
                                                            #Тут походу прям древо стеков, а не просто один стек.

print(quicksort([10, 5, 2, 3, 6, 87 , 34 ,24 , 24, 2]))