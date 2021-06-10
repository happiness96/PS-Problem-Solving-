def solution(s):
    count = 0
    zero_remove = 0
    
    # s가 '1'이 될 때까지 반복
    while s != '1':
        # 제거된 0의 개수 누적
        zero_remove += s.count('0')
        # 1. 문자열 s에서 0을 제거
        s = s.replace('0', '')
        # 2. s의 길이를 c라고 하면,
        # s를 "c를 2진법으로 표현한 문자열"로 바꿉
        c = len(s)
        s = bin(c)[2:]

        count += 1
    
    answer = [count, zero_remove]
        
    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))