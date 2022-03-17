#점수계산
#solved

n= int(input())
score = list(map(int, input().split()))

plus_score = [0] * n

for i in range(n):
    if score[i] == 1:
        plus_score[i] = 1
        if plus_score[i-1] != 0:
            plus_score[i] = plus_score[i-1] + 1

answer = int(sum(plus_score))
print(answer)
