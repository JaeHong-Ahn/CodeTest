N,M = map(int,input().split())
# #10 3
target = list(map(int, input().split()))
#1 2 3

answer = 0
numbers = []

for k in range(N) :
    numbers.append(k+1)

for i in range(M) :
    if numbers[0] != target[i] :
        if numbers.index(target[i]) <= (len(numbers)//2) :
            answer += numbers.index(target[i])
            for _ in range(numbers.index(target[i])) :
                numbers.append(numbers[0])
                numbers.remove(numbers[0])

        elif numbers.index(target[i]) > (len(numbers)//2) :
            while numbers[0] != target[i] :
                numbers.insert(0, numbers[-1])
                numbers.pop()
                answer += 1
        numbers.remove(numbers[0])
    elif numbers[0] == target[i] :
        numbers.remove(target[i])

print(answer)
