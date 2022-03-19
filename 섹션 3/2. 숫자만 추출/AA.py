#숫자만 추출
#solved

import re

inputs = str(input())

#inputs = 'g0en2Ts8eSoft'
finds = re.findall(r"[0-9]", inputs)
number = ''
for each in finds:
    number = number + str(each)

ans_num = int(number)
yaksu = 0
for i in range(1, ans_num +1):
    check = divmod(ans_num,i)
    if check[1] == 0:
        yaksu += 1

print(ans_num)
print(yaksu)
