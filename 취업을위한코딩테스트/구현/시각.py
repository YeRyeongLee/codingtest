def solution(N):
    answer = 0

    # 0 ~ 59까지 3은 일의자리 6개 + 십의자리 10개 - 중복 1 = 15개
    # 시간은 3, 13, 23만 3을 가질 수 있음. 

    # 경우의 수로 생각했을 때 3을 하나라도 가지는 경우의 수는 전체-3을 한개도 가지지 않는 수

    sec = 45
    min = 45

    if N >= 23:
        hour = N-2
    elif N >= 13:
        hour = N-1
    elif N >= 3:
        hour = N
    else:
        hour = N+1
    
    total = (N+1) * 60 * 60
    not3 = hour * min * sec

    answer = total - not3


    return answer


def run():
    N = 5

    print(solution(N))

    return 0


if __name__ == "__main__":
    run()