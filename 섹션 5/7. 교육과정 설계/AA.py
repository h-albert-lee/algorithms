#교육과정 설계
#success

from collections import deque

'''
s = str(input())
n = int(input())
'''
s = 'AKDEF'
n = 1

def check_right(st, lst):
    ans = True
    deq = deque(lst)
    for each in st:
        if each in lst:
            if deq and each == deq[0]:
                deq.popleft()
    if len(deq) != 0:
        ans = False
    return ans

for i in range(n):
    #sample = str(input())
    sample = 'WOPASFKGHDEF'
    if check_right(sample, s):
        print('#%s YES' %(i+1))
    else:
        print('#%s NO' %(i+1))
