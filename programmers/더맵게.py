import heapq

def solution(scoville, K):
    answer = 0
    
    scov_heap = []
    for scov in scoville:
        heapq.heappush(scov_heap, scov)
    
    while len(scov_heap) > 1 and scov_heap[0] < K:
        first = heapq.heappop(scov_heap)
        second = heapq.heappop(scov_heap)
        
        heapq.heappush(scov_heap, first + second*2)
        answer += 1
    
    if not scov_heap or scov_heap[0] < K:
        answer = -1
        
    return answer