#주사위 게임
#solved

n= int(input())

reward = []
max = 0

def rewardcalculate(input):
    from collections import Counter
    money = 0
    check_set = set(input)
    check_list = list(check_set)
    if len(check_list) == 1:
        money = int(check_list[0])*1000 + 10000
    elif len(check_list) == 2:
        often = Counter(input).most_common(1)
        often = often[0][0]
        money = int(often) * 100 + 1000
    else:
        input.sort(reverse = True)
        money = int(input[0])*100
    return money
#rewardcalculate([6,2,5])

for i in range(n):
    K = list(map(int, input().split()))
    money = rewardcalculate(K)
    reward.append(money)

for each in reward:
    if each > max:
        max = each

print(max)
