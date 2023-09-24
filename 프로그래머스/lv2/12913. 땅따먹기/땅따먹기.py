def solution(land) :
    for i in range(1, len(land)) :
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][2], land[i - 1][3], land[i - 1][0])
        land[i][2] += max(land[i - 1][3], land[i - 1][0], land[i - 1][1])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
        
    return max(land[-1])

def solution(land):
    for j in range(1, len(land)):
        land[j][0] += max(land[j-1][1], land[j-1][2], land[j-1][3])
        land[j][1] += max(land[j-1][2], land[j-1][3], land[j-1][0])
        land[j][2] += max(land[j-1][3], land[j-1][0], land[j-1][1])
        land[j][3] += max(land[j-1][0], land[j-1][1], land[j-1][2])

    return max(land[-1])