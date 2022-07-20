
def run():
    n = int(input())
    sanggeun = list(map(int, input().split()))
    
    m = int(input())
    given = list(map(int, input().split()))

    given_dict = {}
    for card in given:
        given_dict[card] = 0
    
    for card in sanggeun:
        if card in given_dict:
            given_dict[card] = 1
    
    for card in given:
        print(given_dict[card], end=' ')

if __name__ == "__main__":
    run()



