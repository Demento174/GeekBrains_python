def main():
    file = open('lesson1.txt','w')
    while True:
        inputString = input('Введите значения, для оставьте строку пустой: ')

        if inputString  == '':
            break

        print(inputString,file=file)
    file.close()


if __name__ == '__main__':
    main()