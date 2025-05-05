from collections import Counter

def solution(topping):
    answer = 0
    cntr = Counter(topping)
    cntr_set = set()
    
    for i in topping:
        cntr[i] -= 1
        cntr_set.add(i)
        if cntr[i] == 0:
            cntr.pop(i)
        if len(cntr) == len(cntr_set):
            answer += 1
    
    return answer