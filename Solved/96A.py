inp = input()

total_zero = 0
total_one = 0

# current_red = 0
# current_green = 0
# current_blue = 0

for x in range(len(inp)):
    checking = inp[x]
    found = False
    count = 1
    # print(checking, count)
    while(found == False):
        
        # print(checking, count)
        if(x+count < len(inp)):
            if(checking == inp[x+count]):
                found = False
                count += 1
            else:
                found = True
        else:
            found = True
    # count -= 1
    
    if(checking == '0'):
        if(count > total_zero):
            total_zero = count
    elif(checking == '1'):
        if(count > total_one):
            total_one = count
            
# print(total_one, total_zero)
if(total_one >= 7 or total_zero >= 7):
    print("YES")
else:
    print("NO")
    
    