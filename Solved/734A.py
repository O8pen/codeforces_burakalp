inp1 = int(input())
inp2 = str(input())

a_count = 0
d_count = 0

for x in inp2:
    if(x == 'A'):
        a_count += 1
    elif(x == 'D'):
        d_count += 1

if(a_count == d_count):
    print('Friendship')
elif(a_count > d_count):
    print('Anton')
elif(a_count < d_count):
    print('Danik')
