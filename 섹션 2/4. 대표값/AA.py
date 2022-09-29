#대표값 again
#wrong answer

N = int(input())
lst = list(map(int, input().split()))
'''
N = 10
lst = [45,73,66,87,92,67,75,79,75,80]
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
print(ans_list)
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
