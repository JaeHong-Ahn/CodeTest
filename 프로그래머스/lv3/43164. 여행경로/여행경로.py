def solution(tickets):
    #airport 출발지 찾음
    def find_start_airport(airport) :
        start = []
        for i in range(len(tickets)) :
            if airport == tickets[i][0] :
                start.append(tickets[i])
        # 알파벳순 정렬
        start = sorted(start, key = lambda x : x[1])
        return start      
    
    def dfs(previous, tickets) :
        
        for i in range(len(tickets)) :
            if tickets[i][0] == previous[0] and tickets[i][1] == previous[1] :
                tickets[i][0] == "visited"
                tickets[i][1] == "visited"
        
        if not find_start_airport(previous[1]) :
            return False
        else :
            next = find_start_airport(previous[1])
        answer.append(previous[1])
        
        if len(set(tickets)) == 1 :
            return answer
        for i in range(len(next)) :
            dfs(next[i], tickets)
    
    answer = ["ICN"]
        
    present = find_start_airport("ICN")
    
    # for i in range(len(present)) :
    #     dfs(present[i], tickets)
    
    print(present)
    
    return answer