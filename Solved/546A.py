strinp = input().split(' ')

k = int(strinp[0])
n = int(strinp[1])
w = int(strinp[2])

amount_needed = 0

for x in range(w):
    amount_needed += k*(x+1)


if(amount_needed-n <= 0):
    print(0)
else:
    print(amount_needed-n)