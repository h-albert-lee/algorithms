#후위표기식 만들기
import re
#s = str(input())
s = '3+5*2/(7-2)'
stack = []


for i in range(len(s)):
    if s[i].isdecimal():
        stack.append(s[i])
    if s[i] == '+' or s[i] == '-':
        if s[i+1].isdecimal()
