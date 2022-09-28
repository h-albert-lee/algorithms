#k번째 큰 수 again

N, k = map(int, input().split())
lst = list(map(int, input().split()))
'''
N = 10
k = 3
lst = [13,15,34,23,45,65,33,11,26,42]
'''
lst.sort(reverse = True)
ans_set = set()

for i in range(N):
    for j in range(i+1, N):
        for l in range(j+1, N):
            sum = lst[i] + lst[j] + lst[l]
            ans_set.add(sum)
ans_list= list(ans_set)
ans_list.sort(reverse=True)
print(ans_list[k-1])
