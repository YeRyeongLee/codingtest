import math

def match(s, e, a, b, match_round):
    n = e - s + 1
    if n == 2:
        return match_round
    
    half = s + n // 2 - 1
    a_bigger = a > half
    b_bigger = b > half
    
    if (int(a_bigger) + int(b_bigger)) == 1:
        return match_round
    else:
        if a_bigger and b_bigger:
            return match(half+1, e, a, b, match_round-1)
        else:
            return match(s, half, a, b, match_round-1)
    
    

def solution(n,a,b):
    answer = 0
    
    match_round = int(math.log2(n))
    answer = match(1, n, a, b, match_round)
    
    return answer