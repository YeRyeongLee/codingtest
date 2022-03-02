def solution(n):
    answer = ''
    
    mapper = {
        1: '1',
        2: '2',
        3: '4'
    }    
    i = 1   # 자릿수
    
    while n:
        remain = (n - 1) % pow(3, i)
        remain += 1
        idx = remain // pow(3, i-1)
        answer = mapper[idx] + answer
        
        n = n - remain
        i += 1
    
    return answer