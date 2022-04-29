#아나그램

a=str(input())
b=str(input())
'''
a = 'AbaAeCe'
b = 'baeeACA'
'''
dict_a = dict()
dict_b = dict()

for i in a:
    dict_a[i] = 0
for i in a:
    e = dict_a[i]
    e += 1
    dict_a[i] = e

for i in b:
    dict_b[i] = 0
for i in b:
    e = dict_b[i]
    e += 1
    dict_b[i] = e

if dict_a == dict_b:
    print('YES')
else:
    print('NO')
