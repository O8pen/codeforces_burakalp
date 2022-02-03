inp = input()

myUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myLower = myUpper.lower()

count_up = 0
count_low = 0
for x in inp:
    if x in myLower:
        count_low +=1
    else:
        count_up +=1
        
if(count_low >= count_up):
    print(inp.lower())
else:
    print(inp.upper())