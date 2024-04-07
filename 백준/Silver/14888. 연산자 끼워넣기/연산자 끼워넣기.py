N = int(input())

nums = list(map(int,input().split()))

op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9

def back_tracking(depth, total, plus, minus, multiply, divide):
    global maximum
    global minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)

    if plus:
        back_tracking(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        back_tracking(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        back_tracking(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        back_tracking(depth + 1, int(total/nums[depth]), plus, minus, multiply, divide - 1)

back_tracking(1, nums[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)