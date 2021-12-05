collection_of_information = lambda name,surname, year, city, email, phone: \
    f"Пользоватль {name} {surname}, {year} года рождения, проживающий в городе {city}, Email: {email}, телефон: {phone}"


if __name__ == '__main__':
    name, surname, year, city, email, phone = [input(f"Введите {i}: ") for i in ['Имя','фамилию', 'год рождения', 'город проживания', 'email', 'Номер телефона']]
    print(collection_of_information(name=name,surname=surname, year= year, city= city, email= email, phone= phone))