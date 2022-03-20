#카드 역배치
#solved

init = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(10):
    n, k = map(int, input().split())
    iternum = (k-n+1)//2
    for each in range(iternum):
        init[n+each], init[k-each] = init[k-each], init[n+each]

init.pop(0)
for i in init:
    print(i, end = ' ')
