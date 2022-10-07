f = open('record.txt','r')
h = open('BA.txt','a')
num = 0
while True:
    line8 = []
    for i in range(8):
        file = f.readline()
        if file == 'finish!!':
            print(succeed)
            num = -1
            break
        else:
            line8.append(file)
    if num == -1:
        break
    for i in range(86):
        unchar = ''
        for j in range(8):
            unchar += line8[j][i]
        sixteen = hex(int(unchar,2))
        sixteen = sixteen[2:]
        if len(sixteen) == 1:
            sixteen = '0' + sixteen
        h.write(sixteen + '')
    line = f.readline()
    if line == '\n':
        num += 1
        print(f'frame:{num}')
f.close()
h.close()
