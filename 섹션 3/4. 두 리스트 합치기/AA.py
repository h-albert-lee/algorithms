#두 리스트 합치기
#time limit exceed

lists = []
for _ in range(4):
    length = int(input())
    lists.append(map(int, input().split()))

lists.sort()

for i in lists:
    print(i, end = ' ')
