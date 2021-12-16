def main():
    file = open('lesson3.txt','r')
    arr = file.readlines()
    print('Сотрудники с зарплатой менее 20 000: ')
    [print(i.split(' ')[0])  for i in arr if float(i.split(' ')[1])<20000]

    middle = 0
    middle=[float(i.split(' ')[1]) for i in arr]
    print('Средняя величина дохода сотрудников: '+str(sum(middle)/len(arr)))
    file.close()


if __name__ == '__main__':
    main()