import random

def bubble_sort(arr):
  n = len(arr)  # Определяем длину списка
  for i in range(n):
    for j in range(0, n - i - 1):  #цикл для сравнения соседних элементов
      print(arr)
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

while True:
    choice = input("1 - вручную , 2 - рандом , 3 - остановить цикл: ")
    if choice == '1':
        answer = list(map(int, input("Введите список цифр через пробел: ").split()))  # преобразуем числа в список
        bubble_sort(answer)
        print(f"Отсортированный список: {answer}")
    elif choice == '2':
        answer = [random.randint(0, 10) for _ in range(10)]  # создаем список из 10 случайных чисел в диапазоне от 0 до 10
        bubble_sort(answer)
        print(f"Отсортированный список: {answer}")
    elif choice == '3':
        break  # прерываем цикл
