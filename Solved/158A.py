inp1 = input().split(' ')
inp2 = input().split(' ')

mini = int(inp2[int(inp1[1])-1])

total = 0
for x in range(int(inp1[0])):
    if int(inp2[x]) >= mini and int(inp2[x]) > 0:
        total += 1
        
print(total)