#사과나무(다이아몬드)
#unsolved

#n=int(input())
#A=[list(map(int, input().split())) for _ in range(n)]

n = 5
A = [[10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]]

center = n//2 + 1
idx = [[] for i in range(n)]

idx_up = idx_down = center
idx_list = []
idx_list.append(center)
contnum = 0

for i in range(n):
    idx[i] = idx_list
    contnum += 1

    if contnum <= center:
        idx_up = idx_up + 1
        idx_down = idx_down -1
    else:
        idx_up = idx_up -1
        idx_down = idx_down +1
    idx_list.append(idx_up)
    idx_list.append(idx_down)
print(idx)
