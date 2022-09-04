def solution(N, ropes):
    answer = 0

    maxWeight = 0

    ropes.sort(reverse=True)

    for i in range(N):
        weight = ropes[i] * (i+1)

        maxWeight = max(maxWeight, weight)
    
    answer = maxWeight

    return answer

def run():
    N = int(input())
    ropes = []

    for _ in range(N):
        ropes.append(int(input()))

    print(solution(N, ropes))

    return 0

if __name__ == "__main__":
    run()