order_dict = {}
sub_course = []

def find_sub(start, order_lst):
    if len(sub_course) >= 2:
        string = "".join(sub_course)
        if string in order_dict:
            order_dict[string] += 1
        else:
            order_dict[string] = 1
    
    if len(sub_course) == len(order_lst):
        return 0
    
    for i in range(start, len(order_lst)):
        sub_course.append(order_lst[i])
        find_sub(i+1, order_lst)
        sub_course.pop()
        
def make_dict(orders):
    for order in orders:
        order_lst = sorted(list(order))
        find_sub(0, order_lst)

def solution(orders, course):
    answer = []
    
    make_dict(orders)
    
    max_dict = {}
    for c in course:
        max_dict[c] = [0, ""]
    
    for menu in order_dict:
        if len(menu) in course and order_dict[menu] >= 2:
            if max_dict[len(menu)][0] < order_dict[menu]:
                max_dict[len(menu)] = [order_dict[menu], menu]
            elif max_dict[len(menu)][0] == order_dict[menu]:
                max_dict[len(menu)].append(menu)
    
    
    for c in max_dict:
        if max_dict[c][0]:
            i = 1
            while i < len(max_dict[c]):
                answer.append(max_dict[c][i])
                i += 1

    answer.sort()
    return answer