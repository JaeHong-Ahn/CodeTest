def solution(numbers, target):
    
    return dfs(numbers, target, 0, 0)

def dfs(numbers, target, sum, current):
    
    cnt = 0
    
    if current == len(numbers) :
        if target == sum:
            return 1
        return 0
    
    cnt += dfs(numbers, target, sum + numbers[current], current+1)
    cnt += dfs(numbers, target, sum + numbers[current] * -1, current+1)
    
    return cnt