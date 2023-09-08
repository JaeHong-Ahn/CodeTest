def solution(word):
    answer = 0
    char = ["A", "E", "I", "O", "U"]
    li = [781, 156, 31, 6, 1]
    #781 = 5^4+5^3+5^2+5^1+5^0
    #156 = 5^3+5^2+5^1+5^0
    #31  = 5^2+5^1+5^0
    #6   = 5^1+5^0
    #1   = 5^0
    for i in range(len(word)):
        answer += (char.index(word[i])) * li[i]
    answer += len(word)
    return answer