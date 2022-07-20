def run():
    n, m = map(int, input().split())
    
    S = []
    for _ in range(n):
        S.append(input())
    
    C = []
    for _ in range(m):
        C.append(input())
    
    S_dict = {}
    for string in S:
        S_dict[string] = 0
    
    for c in C:
        if c in S_dict:
            S_dict[c] += 1
    
    result = 0
    for s in S:
        result += S_dict[s]
    
    print(result)

run()