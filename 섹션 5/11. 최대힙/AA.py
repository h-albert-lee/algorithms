#최대힙
#solved(sol)
import heapq as hq

a = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            ans = hq.heappop(a)
            ans = -ans
            print(ans)
    else:
        hq.heappush(a,-n)
