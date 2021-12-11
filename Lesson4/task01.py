from sys import argv
import argparse
def salary(hours:int,rate:int,bonus:int=0)->int:
    return (hours*rate)+bonus











if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-t','-time',default=argv[0])
    # parser.add_argument('-r', '-rate', default=argv[1])
    # parser.add_argument('-b', '-bonus', default=argv[2])
    # namespace = parser.parse_args(argv)

    print(salary(int(argv[1]),int(argv[2]),int(argv[3])))

