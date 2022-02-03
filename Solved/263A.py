
matrix = []

for x in range(5):
    mini_matrix = []
    line = input().split(' ')
    for i in range(len(line)):
        mini_matrix.append(int(line[i]))
    matrix.append(mini_matrix)
    
    
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == 1:
            print(abs(y-2)+abs(x-2))

# for x in matrix:
#     print(x)