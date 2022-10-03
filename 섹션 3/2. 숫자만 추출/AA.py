#숫자만 추출
#success

word = str(input())

re = str([1,2,3,4,5,6,7,8,9,0])
st = ''
for i in word:
    if i in re:
        st = st+i

num = int(st)

ans = 1

for i in range(1,num):
    if num % i == 0:
        ans += 1
    else:
        pass
print(num)
print(ans)
