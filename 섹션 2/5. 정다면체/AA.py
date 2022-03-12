#정다면체

n, k= map(int, input().split())
#n = 4
#k = 6
from collections import Counter

tar_list = []

for i in range(1,n+1):
    for j in range(1,k+1):
        tar = i+j
        tar_list.append(tar)

tar_count = Counter(tar_list)
ans = tar_count.most_common()
max_count = ans[0][1]
ans_num = 0
for each in ans:
    if each[1] == max_count:
        ans_num += 1

sol = tar_count.most_common(ans_num)
for i in range(len(sol)):
    print(sol[i][0], end = ' ')
