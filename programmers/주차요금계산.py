from math import ceil

def parse(string):
    minutes: int
    carnum: int
    isin: bool
    
    time, carnum, inout = string.split()
    
    h, m = map(int, time.split(":"))
    carnum = int(carnum)
    isin = True if inout == "IN" else False
    
    minutes = h * 60 + m 
    
    return minutes, carnum, isin

def calculate_fee(minutes, fees):
    fee: int
    
    if minutes <= fees[0]:
        fee = fees[1]
    else:
        fee = fees[1]
        minutes -= fees[0]
        
        units = ceil(minutes / fees[2])
        
        fee += units * fees[3]
        
    return fee

def solution(fees, records):
    answer = []
    
    record_dict = {}
    
    for string in records:
        minutes, carnum, isin = parse(string)
        
        if carnum not in record_dict:
            record_dict[carnum] = [True, 0, 0]
        
        if isin:
            record_dict[carnum][0] = True
            record_dict[carnum][1] = minutes
        else:
            record_dict[carnum][0] = False
            record_dict[carnum][2] += minutes - record_dict[carnum][1]
            record_dict[carnum][1] = 0
            
            
    for carnum in sorted(list(record_dict.keys())):
        
        if record_dict[carnum][0]:
            record_dict[carnum][2] += 1439 - record_dict[carnum][1]
            record_dict[carnum][1] = 0
        
        fee = calculate_fee(record_dict[carnum][2], fees)
        
        answer.append(fee)
            
            
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))