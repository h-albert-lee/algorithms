#쇠막대기
#success

laser = str(input())
'''
laser = '()(((()())(())()))(())'
'''
stack = []
cnt = 0

for i in range(len(laser)):
    if laser[i] == '(':
        stack.append(laser[i])
    elif laser[i] == ')':
        stack.pop()
        if laser[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
