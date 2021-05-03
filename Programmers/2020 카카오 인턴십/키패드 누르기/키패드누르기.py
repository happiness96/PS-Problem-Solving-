def solution(numbers, hand):
    answer = ''

    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    
    left = '*'
    right = '#'

    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left = str(number)
        
        elif number in (3, 6, 9):
            answer += 'R'
            right = str(number)
        
        else:
            left_loc = location[left]
            right_loc = location[right]
            number_loc = location[str(number)]

            left_dist = abs(left_loc[0] - number_loc[0]) + abs(left_loc[1] - number_loc[1])
            right_dist = abs(right_loc[0] - number_loc[0]) + abs(right_loc[1] - number_loc[1])

            if left_dist < right_dist:
                answer += 'L'
                left = str(number)
            
            elif left_dist > right_dist:
                answer += 'R'
                right = str(number)
            
            else:
                if hand == 'right':
                    answer += 'R'
                    right = str(number)
                
                else:
                    answer += 'L'
                    left = str(number)
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))