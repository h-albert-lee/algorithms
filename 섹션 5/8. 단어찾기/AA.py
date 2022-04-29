#단어찾기

n = input()
words = {}
for _ in range(n):
    word = input()
    words.add(word)

test = {}
for _ in range(n-1):
    tes = input()
    test.add(tes)

words = list(words)
test = list(test)

for _ in range(len(words)):
    a = words.pop(0)
    b = test.pop(0)
    if a != b:
        print(a)
        break
