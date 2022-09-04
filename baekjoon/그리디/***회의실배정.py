def solution(N, meetings):
    answer = 0

    meeting_time = []
    meeting_dict = {}

    for s, e in meetings:
        meeting_time.append((s, e-s))

        if s not in meeting_dict:
            meeting_dict[s] = []
        meeting_dict[s].append((s, e-s))
    
    


    




    return answer


def run():
    N = int(input())
    meetings = [list(map(int, input().split()))]

    print(solution(N, meetings))

    return 0

if __name__ == "__main__":
    run()
