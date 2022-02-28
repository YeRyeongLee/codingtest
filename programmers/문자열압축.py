import sys
INT_MAX = sys.maxsize


def compress(i, s):
    len_s = 0
    
    ptr = 0
    prev_str = ""
    rep = 1
    
    while ptr < len(s):
        if ptr + i - 1 < len(s):
            sub_str = s[ptr:ptr+i]
        else:
            sub_str = s[ptr:len(s)]
        
        if sub_str == prev_str:
            rep += 1
        else:
            if rep == 1:
                num_str = 0
            else:
                num_str = len(str(rep))
            len_s += num_str + len(prev_str)
            
            prev_str = sub_str
            rep = 1
        
        ptr += i
    
    if rep == 1:
        num_str = 0
    else:
        num_str = len(str(rep))
    len_s += num_str + len(prev_str)
    
    return len_s
            
    
    


def solution(s):
    answer = INT_MAX
    
    for i in range(1, len(s) // 2 + 2):
        answer = min(answer, compress(i, s))
        
    return answer