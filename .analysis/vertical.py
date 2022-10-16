f = open('record2.txt','r')
h = open('sax.txt','a')
num = 0 ; skip = False
while True:
    line8 = []
    for _ in range(8):
        line = f.readline()
        if line == '\n':
            num += 1
            print(f'frame:{num}')
            skip = True
            break
        elif line == 'finish!!':
            print('succeed')
            num = -1
            break
        else:
            line8.append(line)
    if num == -1:
        break
    if skip == True:
        skip = False
    else:
        for i in range(86):
            unchar = ''
            for j in range(8):
                unchar += line8[7-j][i]
            sixteen = int(unchar,2)
            sixteen = hex(sixteen)
            sixteen = sixteen[2:]
            if len(sixteen) == 1:
                sixteen = '0' + sixteen
            sixteen = '0x' + sixteen #今追加したやーつな
            h.write(sixteen + ',')
f.close()
h.close()
