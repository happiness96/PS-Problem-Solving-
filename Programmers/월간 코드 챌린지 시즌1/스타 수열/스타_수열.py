def solution(a):
    counter = {}
    counter_list = set()
    answer = 0
    length = len(a)

    for i in a:
        counter[i] = counter.get(i, 0) + 1
    
    for val, count in counter.items():
        counter_list.add((count, val))

    for count, val in sorted(counter_list, reverse=True):
        if count <= answer:
            break

        chk = [0] * length

        for ind, number in enumerate(a):
            if number == val:
                if ind and not chk[ind - 1] and a[ind - 1] != number:
                    chk[ind] = 1
                    chk[ind - 1] = 1
                
                elif ind != length - 1 and not chk[ind + 1] and a[ind + 1] != number:
                    chk[ind] = 1
                    chk[ind + 1] = 1
        
        answer = max(answer, sum(chk) // 2)

        if count == answer:
            break

    return answer * 2


if __name__ == "__main__":
    print(solution([0]))
    print(solution([5,2,3,3,5,3]))
    print(solution([0,3,3,0,7,2,0,2,2,0]))
    print(solution([2,3,3,2,2,2,2,3]))
    print(solution([3,3,3,3,3]))
    print(solution([1,1]))
    print(solution([1,2,1,1]))
    print(solution([1,2,2,1,3,1,1,4,1]))
    print(solution([2,1,1,1,1,2,3,2,4]))
