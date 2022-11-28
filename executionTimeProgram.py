from ast import main
from mimetypes import init
#import time
from time import time

def func1(a,b):
    #ashu
    return a+b

def func2(a,b):
    #abhay
    num1 = a
    num2 = b
    if (a>b and a!=3):
        pass
    sum([4,3])
    return a+b

if __name__ == '__main__':
    init = time()
    for i in range(0,1000): 
        func1(3,5)
    print("ashu Time:", time() - init)
    init = time()
    for i in range(0,1000): 
        func2(3,5)
    print("abhay Time:", time() - init)
    
    # init = time()
    # for i in range(0,1000): 
    #     func1(3,5)
    # 
    #
    # for i in range(0,1000): 
    #    func2(3,5)
    # print("Overall Time:", time() - init)
    