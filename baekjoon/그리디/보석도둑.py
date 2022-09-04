def solution(N, K, jewels, bags):
    answer = 0
    """
    bagDict = {}

    for weight in bags:
        bagDict[weight] = 0
    
    for M, V in jewels:

    # O(N)이 생각나지 않음...ㅜㅜㅜㅜ
    
    """


    
    return answer

def run():
    inputs = [
        "2 1",
        "5 10",
        "100 100",
        "11",
    ]

    N, K = map(int, inputs[0].split())
    jewels = []
    bags = []

    i = 1

    for _ in range(N):
        M, V = map(int, inputs[i].split())
        jewels.append((M, V))
        i += 1
    
    for _ in range(K):
        C = int(inputs[i])
        bags.append(C)
        i += 1
    
    print(solution(N, K, jewels, bags))

    return 0

if __name__ == "__main__":
    run()

