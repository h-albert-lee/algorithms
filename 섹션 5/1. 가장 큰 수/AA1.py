#가장 큰 수
#solved(sol)
A, n=map(int, input().split())
A = list(map(int, str(A)))
'''
A = str(5276823)
n = int(3)
'''
stack = []

for each in A:
    while stack and n>0 and stack[-1]<each:
        stack.pop()
        n -= 1
    stack.append(each)

if n>0:
    stack = stack[:-n]

ans = ''.join(map(str, stack))
print(ans)
