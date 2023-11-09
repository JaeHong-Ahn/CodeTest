def solution(dirs):
    answer = 0
    U = [0,1]
    D = [0, -1]
    R = [1, 0]
    L = [-1, 0]
    
    maps = [[0,0]]
    
    for i in range(len(dirs)) :
        answer += 1
        now = []
        if dirs[i] == "U":
            now = [maps[-1][0] + U[0], maps[-1][1] + U[1]]
        elif dirs[i] == "D":
            now = [maps[-1][0] + D[0], maps[-1][1] + D[1]]
        elif dirs[i] == "R":
            now = [maps[-1][0] + R[0], maps[-1][1] + R[1]]
        elif dirs[i] == "L":
            now = [maps[-1][0] + L[0], maps[-1][1] + L[1]]
        
        
        if now[0] > 5 or now[0] < -5 or now[1] > 5 or now[1] < -5 :
            answer -= 1
            pass
        else :
            if now in maps:
                now_index = []
                for k in range(len(maps)) :
                    if maps[k] == now :
                        now_index.append(k)
                for j in range(len(now_index)):
                    if now_index[j] >= 1 and maps[now_index[j]-1] == maps[-1] :
                        answer -= 1
                        break
                
                    elif maps[now_index[j]+1] == maps[-1] :
                        answer -= 1
                        break
                    
            maps.append(now)
    return answer