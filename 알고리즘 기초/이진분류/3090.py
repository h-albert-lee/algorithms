#백준 3090번

'''
정수 N개로 이루어진 배열 A가 주어진다. 상근이는 수열의 수 하나를 골라서 값을 1 감소시킬 수 있다.
단, 수는 1보다 작아질 수 없다.

상근이는 위의 감소시키는 연산을 최대 T번 하려고 한다.
이때, 인접한 수의 차이의 최댓값을 최소로 하는 프로그램을 출력하시오.
'''

'''
n, t = map(int, input().split())
A = list(map(int, input().split()))
'''
n = 3
t = 6
A = [10,10,1]

#연산 횟수 함수
def need_operation_num(A, x):
    lst = [A[i] for i in range(len(A)-1)]
    num = 0
    for i in range(0, len(lst)-1):
        if lst[i+1] - lst[i] > x:
            diff = lst[i+1] - (lst[i]+x)
            lst[i+1] = lst[i] + x
            num += diff
    for i in range(len(lst)-1,0,-1):
        if lst[i-1] - lst[i] > x:
            diff = lst[i-1] - (lst[i]+x)
            lst[i-1] = lst[i] + x
            num += diff
    return num

#이진 분류

small = 1
big = int(1e6)
ans = -1

while small <= big:
    mid = int((small+big)//2)
    if need_operation_num(A, mid) <= t:
        big = mid - 1
        ans = mid
    elif need_operation_num(A, mid) > t:
        small = mid + 1
print(ans)
print(A)
for i in range(0, len(A)-1):
    if A[i+1] - A[i] > ans:
        A[i+1] = A[i] + ans
print(A)
for i in range(len(A)-1, 0, -1):
    if A[i-1] - A[i] > ans:
        A[i-1] = A[i] + ans
print(A)
for each in A:
    print(int(each), end = ' ')
