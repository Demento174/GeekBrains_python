
def main():
    fileInput = open('lesson4.1.txt','r')
    fileOutput = open('lesson4.2.txt','w')

    for row in fileInput.readlines():
        fileOutput.write(row.replace('One','Один').replace('Two','Два').replace('Three','Три').replace('Four','Четыре'))
    fileOutput.close()
    fileInput.close()



if __name__ == '__main__':
    main()