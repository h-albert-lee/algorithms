#가장 큰 수
#success
m, n = map(int, input().split())
'''

m = 9977252641
n = 5
'''
m = str(m)
stack = []

for each in m:
    while (n>0) and stack and (stack[-1]<each):
        stack.pop()
        n -= 1
    stack.append(each)

if n>0:
    stack = stack[:-n]

for i in stack:
    print(i, end = '')
