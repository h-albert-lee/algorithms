#증가수열만들기
#solved(sol)

n = int(input())
A = list(map(int, input().split()))

'''

n = 5
A = [2,4,5,1,3]
'''
ans = ''
num = 0
last = 0
lt = 0
rt = n -1
tmp = []
while lt <= rt:
    if A[lt] > last:
        tmp.append((A[lt], 'L'))
    if A[rt] > last:
        tmp.append((A[rt], 'R'))
    if len(tmp) == 0:
        break
    tmp.sort()
    last = tmp[0][0]
    ans = ans + tmp[0][1]
    if tmp[0][1] == 'L':
        lt += 1
    elif tmp[0][1] == 'R':
        rt -= 1
    tmp.clear()

print(len(ans))
print(ans)
