M = int(input())

location = 1

change = []

for i in range(M) :
    change.append(list(map(int,input().split())))

for i in range(M) :
    if location in change[i] :
        change[i].remove(location)
        new_location = change[i][0]
        if new_location > 3 :
            location = -1
            break
        else : location = new_location

print(location)