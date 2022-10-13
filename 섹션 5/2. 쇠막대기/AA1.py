#쇠막대기
#solved(sol)

s = str(input())
#s = '()(((()())(())()))(())'

stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
