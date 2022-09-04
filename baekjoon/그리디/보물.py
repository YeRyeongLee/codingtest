def solution(N, A, B):
    answer = 0

    sump = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(N):
        sump += A[i] * B[i]

    answer = sump
    
    return answer

def run():
    input1 = input()
    input2 = input()
    input3 = input()

    N = int(input1)
    A = list(map(int, input2.split()))
    B = list(map(int, input3.split()))

    print(solution(N, A, B))

    return 0


if __name__ == "__main__":
    run()