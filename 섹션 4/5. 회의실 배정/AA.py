#회의실 배정
#solved(sol)

n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
'''

n = 5
meeting = [(1,4), (2,3), (3,5), (4,6), (5,7)]
'''
meeting.sort(key = lambda x:(x[1], x[0]))

end_time = 0
cnt = 0

for s, e in meeting:
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)
