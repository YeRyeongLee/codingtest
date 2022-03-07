from collections import deque

def solution(s):
    answer = -1
    
    if len(s) % 2 == 1:
        return 0
    
    stack = deque()
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if stack:
        answer = 0
    else:
        answer = 1
    

    return answer