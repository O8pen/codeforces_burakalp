# import random

# # num = int(input())
# num = 3

# lst = []
# small = []

# for y in range(num):
#     small = []
#     for x in range(3):
#         small.append(random.randint(0,1))
#     lst.append(small)
    
# print(lst)

num = int(input())

inputstr = []

for x in range(num):
    inputstr.append(input())
    
total = 0
for x in inputstr:
    spliting = x.split(' ')
    # print(spliting)
    count = 0
    for y in spliting:
        if y == '1':
            count += 1
    if count >= 2:
        total += 1

print(total)