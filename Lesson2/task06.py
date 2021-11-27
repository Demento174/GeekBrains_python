print('Введите товары, для выхода нажмите CTR+D')
products = []
i=1
while True:
    try:
        title = input("Введите название товара: ")
        price=input("Введите цену товара: ")
        quantity =input("Введите количество товара: ")
        unity = input("Введите единицу измерения товара: ")
        products.append(tuple([i,{"название": title, "цена": price, "количество": quantity, "eд": unity}]))
    except EOFError:
        break

characteristics = {index:set([]) for row in products for index,value in row[1].items()}

for row in products:
    for key,item in row[1].items():
        characteristics[key].add(item)
print(characteristics)