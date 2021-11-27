obj = {
    'winter': [1, 2, 12],
    'sprint': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11],
}

month = int(input("Введите месяц: "))
if (1 < month < 12) == False:
    raise "Введите число в диапазоне от 1 до 12"

result = [key for key, value in obj.items() if month in value]

print(result[0])
