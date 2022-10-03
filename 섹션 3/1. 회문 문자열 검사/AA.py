#회문 문자열 검사
#success 

n = int(input())

def test(x):
    x = str(x).lower()
    mid = len(x)//2
    ans = True
    for i in range(0,mid):
        if x[0+i] != x[-1-i]:
            ans = False
    return ans

for i in range(1, n+1):
    word = str(input())
    if test(word) == True:
        print('#%s YES' % (i))
    else:
        print('#%s NO' %(i))
