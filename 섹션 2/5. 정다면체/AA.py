#정다면체 again
#success

n, m = map(int,input().split())
'''
n = 4
m = 6
'''
from collections import Counter
lst = []
for i in range(1, n+1):
    for j in range(1, m+1):
        lst.append(i+j)

ans_list = Counter(lst).most_common()
max_num = ans_list[0][1]

for each in ans_list:
    if each[1] == max_num:
        print(each[0], end = ' ')
