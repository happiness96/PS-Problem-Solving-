def solution(n):
    # 3으로 나눈 나머지를 저장하는 리스트
    save = []
    
    while n:
        # 변환한 3진수를 문자열로 나타낼 것이기 때문에
        # str 형태로 삽입
        save.append(str(n % 3))
        n //= 3
    
    # 거꾸로 읽어들인다
    # -> 이를 다시 앞뒤로 뒤집기 때문에 뒤집을 필요가 없다.
    base_3 = ''.join(save)
    
    # 3진수인 base_3을 10진수로 변환
    answer = int(base_3, 3)
    
    return answer