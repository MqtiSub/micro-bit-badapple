f = open('record2.txt','r')
h = open('record4.txt','a')
num = 0
while True:
    line = f.readline()
    if line == 'finish!!':
        print('succeed')
        break
    if line == '\n':
        num += 1
        h.write('\n')
        print(f'frame:{num}')
    else:
        s = ''
        for i in line:
            s += i
            if len(s) == 8:
                sixteen = hex(int(s,2))
                if len(sixteen) == 3:
                    sixteen = sixteen[:2]+'0'+sixteen[2:]
                h.write(sixteen)
                s = ''
f.close()
h.close()