def solution(numbers, hand):
    answer = ''
    
    num_loc = {
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2)
    }
    for i in range(9):
        num_loc[i+1] = (i//3, i%3)
    
    left_num = [1, 4, 7]
    mid_num = [2, 5, 8, 0]
    right_num = [3, 6, 9]
    
    left_loc = "*"
    right_loc = "#"
    
    for num in numbers:
        if num in left_num:
            left_loc = num
            answer += "L"
        elif num in right_num:
            right_loc = num
            answer += "R"
        else:
            lx, ly = num_loc[left_loc]
            rx, ry = num_loc[right_loc]
            nx, ny = num_loc[num]
            
            distL = abs(lx-nx) + abs(ly-ny)
            distR = abs(rx-nx) + abs(ry-ny)
            
            if distL < distR:
                left_loc = num
                answer += "L"
            elif distR < distL:
                right_loc = num
                answer += "R"
            else:
                if hand == "left":
                    left_loc = num
                    answer += "L"
                else:
                    right_loc = num
                    answer += "R"
        
    return answer