num = int(input())

inputstr = []

for x in range(num):
    inputstr.append(input())
    
for x in inputstr:
    if len(x) > 10:
        print(x[0] + str(len(x)-2) + x[len(x)-1])
    else:
        print(x)