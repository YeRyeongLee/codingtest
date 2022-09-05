DATES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

def solution(x, y):
    answer = ""

    cntDays = 0

    for i in range(1, x):
        cntDays += DATES[i]
    
    cntDays += y

    dayIdx = cntDays % 7

    answer = DAYS[dayIdx]
    
    return answer


def run():
    x, y = map(int, input().split())

    print(solution(x, y))

    return 0

if __name__ == "__main__":
    run()