string = list(input("Введите текст: ").split(" "))
[print(str(i+1)+")"+string[i][:10]) for i in range(len(string))]
