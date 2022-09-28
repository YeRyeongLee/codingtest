import math

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    # n-1까지 확인 시간초과 -> 루트 n 까지만 확인. 
    # O(N^2) -> O(NlogN)
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    
    return True

def toKjinsu_str(n, k):
    result = ""
    
    while n:
        remain = n % k
        n = n // k
        
        result = str(remain) + result
    
    return result

def solution(n, k):
    answer = 0
    
    plist = [i for i in toKjinsu_str(n, k).split('0') if i != ""]
    
    for string in plist:
        num = int(string)

        if isPrime(num):
            answer += 1
            
    return answer


if __name__ == "__main__":
    n = 437674
    k = 3

    print(solution(n, k))
