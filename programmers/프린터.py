from collections import deque

def solution(priorities, location):
    answer = 0
    
    Q = deque()
    printed = 0
    
    for i, p in enumerate(priorities):
        if i == location:
            Q.append((p, 1))
        else:
            Q.append((p, 0))

    while Q:
        curr_p, curr_i = Q.popleft()
        
        prior = False
        for p, i in Q:
            if p > curr_p:
                prior = True
        
        if prior:
            Q.append((curr_p, curr_i))
        else:
            printed += 1
            if curr_i:
                return printed
        
    return answer