#최소힙
#unsolved

A = []
while True:
    s = int(input())
    if s == 0:
        print(min(A))
        A = []
    elif s == -1:
        break
    else:
        A.append(s)
