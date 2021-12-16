def main():
    file = open('lesson2.txt','r')
    text = file.readlines()

    yield len(text)
    for i in text:
        yield len(i.replace('\n',''))
    file.close()


if __name__ == '__main__':
    i = 0
    for iter in main():
        print(f'количество строк: {iter}'if i == 0 else f"В строке номер {i}: {iter} количество слов")
        i+=1