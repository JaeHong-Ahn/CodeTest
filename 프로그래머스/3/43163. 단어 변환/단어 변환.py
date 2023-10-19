def recursion(words, word, target, visited, cnt, result) :
    if word == target :
        result.append(cnt)
        return

    if visited[words.index(word)] == False :
        visited[words.index(word)] = True
        cnt += 1

        for i in range(len(words)) :
            if visited[i] == False and count_different_chars(word, words[i]) == 1:
                recursion(words, words[i], target, visited, cnt, result)
                visited[i] = False

def count_different_chars(word1, word2):
    diff_count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1

    return diff_count

def solution(begin, target, words):
    result = []
    answer = 0
    visited = [False] * len(words)
    for i in range(len(words)) :
        if count_different_chars(begin, words[i]) == 1 :
            recursion(words,words[i], target, visited, answer, result)

    if len(result) == 0 :
        return 0
    else :
        return min(result) + 1