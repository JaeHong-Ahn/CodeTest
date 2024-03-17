
numbers = []
all_num = []
answer = []

for i in range(1, 10000) :
    one = i % 10
    ten = 0
    hun = 0
    tho = 0

    if i >= 10 :
        ten = (i // 10) % 10

    if i >= 100 :
        hun = (i // 100) % 10

    if i >= 1000:
        tho = (i // 1000) % 10

    num = i + one + ten + hun + tho

    all_num.append(i)

    if num not in numbers and num <= 10000:
        numbers.append(num)

answer = list(set(all_num).difference(set(numbers)))
answer.sort()

for a in answer:
    print(a)