def compress(arr, start_row, start_col, length):
    if length == 1:
        if arr[start_row][start_col] == 0:
            return [1, 0]
        
        else:
            return [0, 1]
    
    number = arr[start_row][start_col]
    flag = 1    # 압축이 가능하면 1, 불가능하면 0

    for row in range(start_row, start_row + length):
        for col in range(start_col, start_col + length):
            if arr[row][col] != number:
                flag = 0
                break
        
        if not flag:
            break
    
    if flag:    # 압축이 가능할 경우
        if number:
            return [0, 1]
        
        else:
            return [1, 0]
    
    else:       # 압축이 불가능한 경우 분할정복
        result = []

        length //= 2
        result.append(compress(arr, start_row, start_col, length))
        result.append(compress(arr, start_row + length, start_col, length))
        result.append(compress(arr, start_row, start_col + length, length))
        result.append(compress(arr, start_row + length, start_col + length, length))

        return_value = [0, 0]

        for zero, one in result:
            return_value[0] += zero
            return_value[1] += one
        
        return return_value


def solution(arr):
    N = len(arr)
    answer = compress(arr, 0, 0, N)

    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
