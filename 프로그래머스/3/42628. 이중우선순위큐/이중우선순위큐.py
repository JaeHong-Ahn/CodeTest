def solution(operations):
    answer = []
    alpha = []
    nums = []

    for o in operations:
        a, b = o.split()

        alpha.append(a)
        nums.append(b)

    for i in range(len(nums)):
        if alpha[i] == 'I':
            answer.append(int(nums[i]))
        
        if alpha[i] == 'D' and len(answer) > 0:
            if nums[i] == '1':
                answer.remove(max(answer))

            if nums[i] == '-1' and len(answer) > 0:
                answer.remove(min(answer))

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]