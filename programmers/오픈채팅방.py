def solution(record):
    answer = []
    
    id_name = {}
    
    for string in record:
        cmd = list(string.split())
        
        if cmd[0] == "Enter":
            id_name[cmd[1]] = cmd[2]
        elif cmd[0] == "Change":
            id_name[cmd[1]] = cmd[2]
    
    for string in record:
        cmd = list(string.split())
        
        if cmd[0] == "Enter":
            answer.append(id_name[cmd[1]]+"님이 들어왔습니다.")
        elif cmd[0] == "Leave":
            answer.append(id_name[cmd[1]]+"님이 나갔습니다.")
            
    
    return answer