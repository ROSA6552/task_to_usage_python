from decimal import Decimal

string = input()
a = 0
b = 0
index = 0
aft_p = ''

for i in range(0, len(string)):
    if string[i] != '/':
        a *= 10
        a += Decimal(string[i])
    if string[i] == '/':
        index = i + 1
        break

for i in range(index, len(string)):
    b *= 10
    b += Decimal(string[i])

c = str(a / b)
c_tsel = int(c) // 1

for i in range(0, len(c)):
    if (c[i] == '.'):
        index = i + 1       #index of first number after point
        break

if index != 0:
    print(int(c_tsel), '.(')
    for i in range(index, len(c) - 1):
        for j in range(i + 1, len(c)):
            if (c[i] == c[j]):
                for k in range(i, j):
                    if k[i] != k[j]:
                        break
                    aft_p += k[i]
                if (aft_p )    

print(c)
