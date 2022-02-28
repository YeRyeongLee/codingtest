def solution(numbers):
    answer = 0
    
    freq = [0 for _ in range(10)]
    
    for num in numbers:
        freq[num] = 1
    
    for i in range(10):
        if not freq[i]:
            answer += i
    
    return answer