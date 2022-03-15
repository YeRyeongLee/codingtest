# 로직이 틀림. 
# BFS로 작은 후보키부터 확인. -> 큰 후보키 안에 작은 후보키 있으면 나가리. 

def is_candidate(relation, comb):
    tuples = {}
    
    for row in relation:
        tup = []
        for j in range(len(relation[0])):
            if j in comb:
                tup.append(row[j])
                
        if tup in tuples:
            return False
        else:
            tuples[tup] = 1
    
    return True
    
    

def find_candidates(relation, comb, start):
    # start부터의 컬럼만 고려. 
    if len(comb) > 0 and is_candidate(relation, comb):
        return 1
    elif len(comb) == len(relation[0]):
        return 0
    
    candidates = 0
    
    for i in range(start, len(relation[0])):
        comb.append(i)
        candidates += find_candidates(relation, comb, start)
        comb.pop()
    
    return candidates
    

def solution(relation):
    answer = 0
    comb = []
    answer = find_candidates(relation, comb, 0)
    return answer
    

def solution(relation):
    answer = 0
    comb = []
    answer = find_candidates(relation, comb, 0)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))

lst = [["1", "1", "1"], ["1", "1", "2"], ["1", "1", "3"], ["1", "1", "4"], ["1", "1", "5"]]