import random

def writeIn():
    randomArr = [str(random.randint(1, 1001)) for i in range(random.randint(5, 11))]
    ' '.join(randomArr)
    arrToStr = ' '.join(randomArr)
    fileInput = open('lesson5.txt','w')
    fileInput.write(arrToStr)

    fileInput.close()

def readOf():
    fileInput = open('lesson5.txt', 'r')
    row = fileInput.readlines()[0]
    arr = [int(i) for i in row.split(' ')]
    print('Общая сумма в файле: '+str(sum(arr)))
    fileInput.close()

if __name__ == '__main__':
    writeIn()
    readOf()