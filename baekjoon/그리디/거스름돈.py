NUM_OF_BILLS = 6
BILLS = [500, 100, 50, 10, 5, 1]
PAY = 1000

def solution(price):
    answer = 0

    change = PAY - price

    for i in range(NUM_OF_BILLS):
        answer += change // BILLS[i]
        change = change % BILLS[i]

    return answer

def run():
    
    price = int(input())

    print(solution(price))

    return 0

if __name__ == "__main__":
    run()
