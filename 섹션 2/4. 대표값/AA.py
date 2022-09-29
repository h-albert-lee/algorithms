#대표값 again
#success

N = int(input())
lst = list(map(int, input().split()))
'''
N = 15
lst = [12,34,17,6,11,15,27,42,39,31,25,36,35,25,17]
'''

mean = round(sum(lst)/len(lst))

diff_list = []
ans_list = []
ans_list_index = []

min_diff = 1000000
for i, j in enumerate(lst):
    diff = abs(j - mean)
    if diff < min_diff:
        min_diff = diff
        ans_list = []
        ans_list_index = []
    if diff == min_diff:
        ans_list.append(j)
        ans_list_index.append(i)

res_list = []
res_list_index =[]
max = 0
for index, value in enumerate(ans_list):
    if value > max:
        max = value
        res_list = []
        res_index = []
    if value == max:
        res_list.append(value)
        res_index.append(index)
number = ans_list_index[res_index[0]] +1

print('%s %s' %(mean, number ) )
