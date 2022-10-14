from collections import Counter
#success

s1 = str(input())
a1 = dict(Counter(s1))

s2 = str(input())
a2 = dict(Counter(s2))

if a1==a2:
    print('YES')
else:
    print('NO')
