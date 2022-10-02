#자릿수의 합
#success

n = int(input())
lst = list(map(int, input().split()))
'''
n = 3
lst = [125, 15232, 97]
'''
def digit_sum(x):
    sum = 0
    x = str(x)
    for each in x:
        sum += int(each)
    return sum

max = 0
max_num = 0
for i in lst:
    if digit_sum(i) > max:
        max = digit_sum(i)
        max_num = i

print(max_num)
