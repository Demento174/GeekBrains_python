import json
def main():
    firms = {}
    average_profit = []
    with open('lesson7.txt', 'r') as file:
        rows = [i.split(' ') for i in file.read().split('\n')]
        for i in rows:
            result = int(i[2])- int(i[3])
            firms[i[0]]= result
            if result > 0:
                average_profit.append(result)
        average_profit = {'average_profit':round(sum(average_profit)/len(average_profit))}
        with open('lesson7.json', 'w') as f:
            f.write(json.dumps([firms,average_profit]))

        with open('lesson7.json') as f:
            print(f.read())

if __name__ == '__main__':
    main()