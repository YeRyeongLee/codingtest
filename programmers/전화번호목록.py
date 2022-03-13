def is_prefix(phone_book, idx):
    # idx부터 시작해서 접두어인 경우가 있는지
    
    num_dict = {}
    for i in range(10):
        num_dict[i] = []
        
    for number in phone_book:
        if len(number) == idx:
            return True
        else:
            num_dict[int(number[idx])].append(number)
    
    prefix = False
    for key in num_dict:
        if len(num_dict[key]) >= 2:
            if is_prefix(num_dict[key], idx+1):
                prefix = True
    
    return prefix

def solution(phone_book):
    answer = True
    
    answer = not is_prefix(phone_book, 0)
    
    return answer