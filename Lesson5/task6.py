
def main():
    file = open('lesson6.txt','r')
    obj = {}
    for i in file.readlines():

        i = i.replace('—','')\
            .replace('(л)','')\
            .replace('(пр)','')\
            .replace('(лаб)','')\
            .replace('\n','').split(' ')
        key = i[0]
        i.remove(key)
        i = [int(n) for n in i if n != '']
        obj[key]=sum(i)
    file.close()
    print(obj)



if __name__ == '__main__':
    main()