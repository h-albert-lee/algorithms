#씨름 선수
#success

n = int(input())
A = []
for _ in range(n):
    s, e = map(int, input().split())
    A.append((s,e))
'''

n = 5
A = [(172, 67), (183, 65), (180, 70), (170,72), (181,60)]
'''
A.sort(key = lambda x : (x[1], x[0]), reverse =True)
cnt = 1
h1, w1 = A.pop(0)

for h, w in A:
    if (h < h1) and (w < w1):
        pass
    else:
        cnt += 1
        h1 = h
        w1 = h
print(cnt)
