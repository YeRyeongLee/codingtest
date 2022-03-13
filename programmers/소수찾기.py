def is_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            if i*i <= n and n % i == 0:
                return 0
        return 1

def find_comb(numbers, comb, primes): # comb에는 숫자의 인덱스 저장
    if not comb:
        cnt = 0
    else:
        n = int(''.join([numbers[i] for i in comb]))
        if n in primes:
            cnt = 0
        else:
            primes.append(n)
            cnt = is_prime(n)
        
        if len(comb) == len(numbers):
            return cnt
    
    for i in range(len(numbers)):
        if i not in comb:
            comb.append(i)
            cnt += find_comb(numbers, comb, primes)
            comb.pop()
    
    return cnt
    
def solution(numbers):
    answer = find_comb(numbers, [], [])
    return answer