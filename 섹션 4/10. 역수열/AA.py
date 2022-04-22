#역수열
#unsolved
'''
n = int(input())
A = list(map(int, input().split()))
'''

n = 8
A = [5,3,4,0,2,1,1,0]

cand_list = list(range(1,n+1))
blank_list = [n]*n

def checker(position, number, lst):
    ans = True
    for each in lst[:position]:
        if each < number:
            ans = False
    return ans

def counter(position, number, lst):
    cnt = 0
    for each in lst[:position-1]:
        if each < number:
            cnt += 1
    return cnt


for i, v in enumerate(A):
    cand_num = i + 1
    if checker(v, cand_num, blank_list):
        blank_list[v] = cand_num
    else:
        cnt = counter(v,cand_num,blank_list)
        blank_list[v+cnt] = cand_num

print(blank_list)
