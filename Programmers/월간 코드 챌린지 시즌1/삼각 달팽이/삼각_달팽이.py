def solution(n):
    triangle_list = [[0] * i for i in range(1, n + 1)]
    
    number = 1
    flag = 0    # 왼쪽 0, 아래쪽 1, 오른쪽 2
    row, col = -1, 0
    
    for count in range(n, 0, -1):
        if flag == 0:
            for _ in range(count):
                row += 1
                triangle_list[row][col] = number
                number += 1
        
        elif flag == 1:
            for _ in range(count):
                col += 1
                triangle_list[row][col] = number
                number += 1
        
        else:
            for _ in range(count):
                row -= 1
                col -= 1
                triangle_list[row][col] = number
                number += 1
            
        flag = (flag + 1) % 3
    
    answer = []
    
    for t_list in triangle_list:
        answer.extend(t_list)
    
    return answer


print(solution(4))
print(solution(5))
print(solution(6))