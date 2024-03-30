#일곱 난쟁이
height = []

for _ in range(9):
    height.append(int(input()))

target = sum(height) - 100
target_nums = []

for i in range(len(height)-2):
    for j in range(i+1, 9):
        if (height[i] + height[j]) == target:
            target_nums.append(i)
            target_nums.append(j)

        else: pass

height.remove(height[target_nums[0]])
height.remove(height[target_nums[1]-1])

height.sort()

for h in height:
    print(h)