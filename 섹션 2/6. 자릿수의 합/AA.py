n= map(int, input())
K = list(map(int, input().split()))

def digit_sum(K):
    check_num = []
    for each in K:
        sum_num = 0
        nums = each
        for i in range(1,10):
            div_num = 100000000/(10**i)
            a,b = divmod(nums, div_num)
            sum_num = sum_num + a
            nums = nums - a*div_num
        check_num.append(sum_num)
    max = 0
    index = 0
    for each in range(len(check_num)):
        if check_num[each] > max:
            max = check_num[each]
            ans = K[each]
    return ans

print(digit_sum(K))
