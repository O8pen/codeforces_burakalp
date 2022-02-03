num_of_inp = int(input())

command_list = []

for x in range(num_of_inp):
    command_list.append(input())
    
result = 0
for x in command_list:
    if(str(x).lower() == 'x++' or str(x).lower() == '++x'):
        result += 1
    else:
        result -= 1
        
print(result)