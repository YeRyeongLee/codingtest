from collections import deque

def solution(progresses, speeds):
    answer = []
    
    p_que = deque()
    
    for p, s in zip(progresses, speeds):
        p_que.append([p, s])
    
    while p_que:
        
        # 진도 나가기
        for i in range(len(p_que)):
            p_que[i][0] += p_que[i][1]
        
        # 100프로 이상인거 배포
        distrib = 0
        while p_que and p_que[0][0] >= 100:
            p_que.popleft()
            distrib += 1
        
        if distrib:
            answer.append(distrib)
    
    return answer