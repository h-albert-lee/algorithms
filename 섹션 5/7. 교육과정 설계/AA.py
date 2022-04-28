#교육과정설계

from collections import deque

a = str(input())
num = int(input())
'''
a = 'ACF'
num = 1
'''
lu = []
for each in a:
    lu.append(each)


for n in range(num):
    que = deque(lu)
    check = str(input())
    #check = 'AFFDCCFF'
    for i in check:
        try:
            if que[0] == i:
                que.popleft()
        except:
            pass
    if len(que) == 0:
         print("#%d YES" %(n+1))
    else:
        print("#%d NO" %(n+1))
