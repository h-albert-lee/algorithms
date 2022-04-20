#씨름선수
#solved

n = int(input())
meeting = []
for _ in range(n):
    h, w = map(int, input().split())
    meeting.append((h,w))
'''

n = 5
meeting = [(172,67), (183,65), (180,70), (170,72), (181,60)]
'''
#첫번째 방법

meeting.sort(reverse = True)

cnt = 0
pointer_h = meeting[0][0]
pointer_w = meeting[0][1]

for h, w in meeting:
    if (h < pointer_h) and (w < pointer_w):
        cnt += 1

    else:
        pointer_h = h
        pointer_w = w

ans = n - cnt
print(ans)
