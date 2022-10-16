f = open('record.txt','r')
h = open('badapple.txt','a')

num = 0 ; flag = False
while True:
    line = f.readline()
    if line == '\n':
        num += 1
        print(f'frame:{num}')
    elif line == 'finish!!':
        print('succeed!!')
        break
    else:
        while True:
            if len(line) < 10:
                count = len(line) -1
                line = line[:-1]
                for i in range(8-count):
                    line += '0'
                flag = True
                sixteen = int(line,2)
            else:
                unchar = ''
                for i in range(8):
                    unchar += line[i]
                sixteen = int(unchar,2)
                line = line[8:]
            sixteen = hex(sixteen)
            sixteen = sixteen[2:]
            if len(sixteen) == 1:
                sixteen = '0' + sixteen
            h.write(sixteen + ' ')
            if flag == True:
                flag = False
                break
f.close()
h.close()