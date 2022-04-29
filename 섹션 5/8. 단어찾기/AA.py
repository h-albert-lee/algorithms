#단어찾기
#solved(sol)

n = int(input())
words = dict()
for i in range(n):
    k = input()
    words[k] = 0
for i in range(n-1):
    k = input()
    words[k] = 1

for i, v in words.items():
    if v == 0:
        print(i)
        break
