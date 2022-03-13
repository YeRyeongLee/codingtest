from math import gcd

def solution(w,h):
    answer = 1
    broken = w + h - gcd(w, h)
    answer = w*h - broken
    return answer