inp = input().split(' ')

n = int(inp[0])
k = int(inp[1])

while(k > 0):
    if(n%10 == 0):
        n = n/10
    else:
        n -= 1
    k -= 1

print(int(n))