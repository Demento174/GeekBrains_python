arr = [10,7, 5, 3, 3, 2]
print("Входной массив: ",arr)
while True:
    value = int(input('Введите число:'))
    arr_index = None
    if value in arr:
        arr_index = [i + 1 for i in range(len(arr)) if arr[i] == value][-1]
    else:

        if value < min(arr):
            arr_index = len(arr)
        elif value > max(arr):
            arr_index = 0
        else:
            arr_index = [count + 1 for count, item in enumerate(arr) if item > value > arr[count + 1]][0]

    arr.insert(arr_index, value)
    print(arr)

