# 피보나치 함수

T = int(input())
nums = []
fibo_0 = [1, 0, 1]
fibo_1 = [0, 1, 1]

for _ in range(T):
    nums.append(int(input()))


def fibo(n):
    if n >= len(fibo_0):
        for i in range(len(fibo_0), n + 1):
            fibo_0.append(fibo_0[i - 1] + fibo_0[i - 2])
            fibo_1.append(fibo_1[i - 1] + fibo_1[i - 2])
    print(fibo_0[n], fibo_1[n])


for num in nums:
    fibo(num)
