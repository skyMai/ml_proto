import sys
import math
from collections import Iterable

def main():
    val =(31,452,65)
    if isinstance(val,Iterable):
        print("tuple is Iterable")
    else:
        print('not Iterable')
    
if __name__ == '__main__':
    main()