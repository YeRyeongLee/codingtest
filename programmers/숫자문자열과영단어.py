def solution(s):
    answer = 0
    ans_str = ""
    
    num_arr = [str(num) for num in range(10)]
    num_dict = {'zero': 0,
               'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9}
    
    idx = 0
    while idx < len(s):
        if s[idx] in num_arr:
            ans_str += s[idx]
            idx += 1
        else:
            if idx+2 < len(s) and s[idx:idx+3] in num_dict:
                ans_str += str(num_dict[s[idx:idx+3]])
                idx += 3
            elif idx+3 < len(s) and s[idx:idx+4] in num_dict:
                ans_str += str(num_dict[s[idx:idx+4]])
                idx += 4
            elif idx+4 < len(s) and s[idx:idx+5] in num_dict:
                ans_str += str(num_dict[s[idx:idx+5]])
                idx += 5
    
    answer = int(ans_str)
    return answer