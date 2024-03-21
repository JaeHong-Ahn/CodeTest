N = int(input())

A = list(map(int, input().split()))

B, C = map(int, input().split())

# 총 감독관 = 시험장의 개수 N -> 각 시험장에서 B 만큼 뺌

answer = 0 # 부 감독관의 수

for i in range(N) :
    if B >= A[i] :
        pass
    else :
        A[i] -= B
        if A[i] % C == 0 :
            answer += (A[i] // C)
        else :
            answer += ((A[i] // C) + 1)

print(answer + N)