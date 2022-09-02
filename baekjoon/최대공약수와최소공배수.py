import math
from xmlrpc.client import MAXINT

def max_gongyaksu(a, b):
    max = 1

    for i in range(2, math.sqrt(max(a, b))):
        if a%i == 0 and b%i == 0:
            max = i

    return max

def min_gongbaesu(a, b):
    min = MAXINT
    
    return min


def run():
    a, b = map(int, input().split())
    print(max_gongyaksu(a, b))
    print(min_gongbaesu(a, b))
