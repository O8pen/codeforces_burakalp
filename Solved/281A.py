inp = input()

new = ''

for id, x in enumerate(inp):
    # print(id, x.upper())
    if id == 0:
        new = new + str(x).upper()
    else:
        new = new + x

print(new)