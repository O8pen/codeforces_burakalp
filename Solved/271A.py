inp1 = str(input())

anan = False

while(anan == False):
    inp1 = str(int(inp1)+1)

    if(inp1[0] != inp1[1] and inp1[0] != inp1[2] and inp1[0] != inp1[3] and inp1[1] != inp1[2] and inp1[1] != inp1[3] and inp1[2] != inp1[3]):
        anan = True

print(inp1)
