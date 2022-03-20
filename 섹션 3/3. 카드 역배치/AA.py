#카드 역배치
#unsolved

init = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
check_number = 0

n, k = map(int, input().split())


init_list = init[n:k+1]
change_list = [0]*len(init_list)
for i in range(len(init_list)):
    init_list_num = len(init_list) -1 - i
    change_list[i] = init_list[init_list_num]

init[n:k+1] = change_list
check_number = check_number +1

if check_number == 10:
    for i in range(1,21):
        print(init[i], end = ' ')
