#k번째 약수
#solved

n, k= map(int, input().split())

answer_list = []

for i in range(1,n+1):
    if n % i == 0:
        answer_list.append(i)
try:
    answer = answer_list[k-1]
except:
    answer = -1

print(answer)
