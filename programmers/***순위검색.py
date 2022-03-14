# 효율성테스트 통과 못함

def check(checked, checking):
    if checked == checking:
        return 1
    else:
        return 0
    
def solution(info, query):
    answer = []
    
    info_list = [list(string.split()) for string in info]
    
    for q in query:
        q = list(q.split())
        
        qualified = [1 for _ in range(len(info_list))]
        
        for j in range(0, 7, 2):
            checking = q[j]
            
            if checking == '-':
                continue
            
            for i in range(len(info_list)):
                checked = info_list[i][j//2]
                
                if qualified[i]:
                    qualified[i] = check(checked, checking)
        
        for i in range(len(info_list)):
            if qualified[i]:
                qualified[i] = int(int(q[7]) <= int(info_list[i][4]))
                pass
        
        answer.append(sum(qualified))
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = [1,1,1,1,2,4]

print(solution(info, query))