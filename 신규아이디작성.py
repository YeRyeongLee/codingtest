def is_proper(char):
    if char in '~!@#$%^&*()=+[{]}:?,<>/':
        return False
    else:
        return True
        

def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    temp_id = ""
    for i in range(len(new_id)):
        char = new_id[i]
        if is_proper(char):
            temp_id += char
    new_id = temp_id
    
    # 3
    if new_id:
        temp_id = new_id[0]
        for i in range(1, len(new_id)):
            if new_id[i] == "." and new_id[i-1] == ".":
                pass
            else:
                temp_id += new_id[i]
        new_id = temp_id
    
    # 4
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 5
    if not new_id:
        new_id = "a"
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    
    # 7
    if len(new_id) <= 2:
        char = new_id[-1]
        while len(new_id) <= 2:
            new_id += char
    
    answer = new_id
    return answer