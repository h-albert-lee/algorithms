#후위식 연산
#solved
s = str(input())
#s = '352+*9-'
list_s = []
for i in s:
    list_s.append(i)

stack = []
for each in list_s:
    if each.isdecimal():
        k = int(each)
        stack.append(k)
    elif each == '+':
        b = stack.pop()
        a = stack.pop()
        k = a+b
        stack.append(k)
    elif each == '-':
        b = stack.pop()
        a = stack.pop()
        k = a-b
        stack.append(k)
    elif each == '*':
        b = stack.pop()
        a = stack.pop()
        k = a*b
        stack.append(k)
    elif each == '/':
        b = stack.pop()
        a = stack.pop()
        k = a/b
        stack.append(k)


print(stack[0])
