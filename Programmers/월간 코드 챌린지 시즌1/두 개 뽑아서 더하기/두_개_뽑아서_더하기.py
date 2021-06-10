from itertools import combinations

def solution(numbers):
    answer = set()
    
    for case in combinations(numbers, 2):
        total = sum(case)
        
        answer.add(total)
    
    answer = sorted(answer)
    
    return answer
