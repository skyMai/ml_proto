
import sys
import math

class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable
        
def math_func(intArg,defaultInt=5):
    result = int(intArg)*defaultInt+3
    print("result is %(result)s, intArg is %(intArg)s" % {'result':result, 'intArg':intArg})

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def main():
    # input("please input your number:")
    # print("you input %s" % sys.argv)
    # argc = len(sys.argv)
    # if argc == 2:
    #     math_func(sys.argv[1])
    # elif argc ==3:
    #     math_func(sys.argv[1]+sys.argv[2])
    dict = {'hello':241,'wht':42, "j":[32,4,3]}



if __name__ == "__main__":
    main()