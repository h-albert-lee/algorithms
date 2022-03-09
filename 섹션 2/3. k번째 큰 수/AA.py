n, k= map(int, input().split())
N = list(map(int, input().split()))
ans_list = []
for i in range(n):
    for k in range(n):
        for j in range(n):
            ans = N[i] + N[k] + N[j]
            ans_list.append(ans)
ans_list.sort()
ans_set = set(ans_list)
ans = int(ans_set[k-1])
print(ans)
