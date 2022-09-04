def solution(N, scores):
    answer = 0

    scores.sort(key=lambda x: x[0])

    minMyeonjup = scores[0][1]+1

    for _, myeonjup in scores:
        if myeonjup < minMyeonjup:
            answer += 1
        minMyeonjup = min(minMyeonjup, myeonjup)

    return answer


def run():
    T = int(input())


    for _ in range(T):
        N = int(input())

        scores = []

        for _ in range(N):
            score1, score2 = map(int, input().split())
            scores.append((score1, score2))
        
        print(solution(N, scores))
    
    return 0


if __name__ == "__main__":
    run()

