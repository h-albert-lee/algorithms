'''
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.
'''

'''
N = int(input)
k = int(input)
'''
lst = [1,2,3,4,5,6,7,8,9]
for i in range(0, len(lst)-1):
    print(i)
    print('lst는', lst[i])
print('----------------------')
for i in range(len(lst)-1,0,-1):
    print(i)
    print('lst는', lst[i])
