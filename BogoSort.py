import random


def sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True



def shuffle_array(arr):
    random.shuffle(arr)


def bogoSort(arr):
    while not sorted(arr):
        shuffle_array(arr)
        print(arr)
    return arr


array = [3,2,4,1]
print(f"Изначальный массив : {array}")
sorted_array = bogoSort(array)
print(f"Массив после сортировки BogoSort : {sorted_array}")




