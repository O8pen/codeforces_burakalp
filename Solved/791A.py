strinp = input().split(' ')

a = int(strinp[0])
b = int(strinp[1])

count = 0
while(a <= b):
    a = a*3
    b = b*2
    count+=1

print(count)