#회문 문자열 검사
#solved

n= int(input())

def takereverse(input):
    inputs = str(input)
    length = len(input)-1
    reversed = ''
    for each in range(length,-1,-1):
        reversed = reversed + inputs[each]
    return reversed

for i in range(1,n+1):
    words = str(input())
    words = words.lower()
    reversed_words = takereverse(words)
    ans = ''
    if words == reversed_words:
        ans = 'YES'
    else:
        ans = 'NO'
    print('#%d %s' %(i, ans))
