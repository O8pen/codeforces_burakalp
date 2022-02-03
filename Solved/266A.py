inp1 = int(input())
inp2 = input()

total_red = 0
total_green = 0
total_blue = 0

# current_red = 0
# current_green = 0
# current_blue = 0

res = 0

for x in range(inp1-1):
    if(inp2[x] == inp2[x+1]):
        res += 1
            
print(res)
    