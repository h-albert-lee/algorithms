#후위표기식 만들기
#solved(sol)
s = str(input())
#s = '3+5*2/(7-2)'
stack = []
ans = ''


for i in range(len(s)):
    if s[i].isdecimal():
        ans += s[i]
    else:
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == '*' or s[i] == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(s[i])
        elif s[i] == '+' or s[i] == '-':
            while stack and (stack[-1] != '('):
                ans += stack.pop()
            stack.append(s[i])
        elif s[i] == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)
