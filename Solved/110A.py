inp1 = list(input())


correct = 'NO'

count4 = inp1.count('4')
count7 = inp1.count('7')

count_digits = count7 + count4

if(count_digits == 4 or count_digits ==7):
    correct = 'YES'

        
print(correct)