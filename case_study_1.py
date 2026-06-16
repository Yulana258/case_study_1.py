 def sum_between_min_max(arr): 
            """
      Находит сумму отрицательных элементовмежду минимальным и максимальным элементами массива.
      Args:
      arr: список чисел (одномерный массив)
      Returns:
      Сумма отрицательных элементов между min и max, или 0, если таких элементов нет
      """
      if not arr: # Проверка на пустой массив
      return 0
      # Находим индексы минимального и максимального элементов
      min_idx = arr.index(min(arr))
      max_idx = arr.index(max(arr))
      Определяем границы диапазона (от меньшего к большему)
      start = min(min_idx, max_idx)
      end = max(min_idx, max_idx)
      # Суммируем отрицательные элементы в диапазоне (не включая min и max)
      sum_negative = 0
     for i in range(start + 1, end):
          if arr[i] < 0:
              sum_negative += arr[i]
      return sum_negative
      # Пример использования
      if__name__=="__main__":
        # Тестовыне данные 
          A = [-7, 3, -2, 5, -8, 1, -4, 9, -1, 2, 10]
  result = sum_between_min_max(A)
  print(f"Массив: {A}")
  print(f"Сумма отрицательных элементов между min и max: {result}")