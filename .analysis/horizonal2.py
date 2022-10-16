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
        unchar = ''
        for i in line:
            unchar += i
            if len(unchar) == 8:
                sixteen = int(unchar,2)
                sixteen = hex(sixteen)
                sixteen = sixteen[2:]
                if len(sixteen) == 1:
                    sixteen = '0' + sixteen
                h.write(sixteen + ' ')
                unchar = ''
        unchar = unchar[:-1]
        for _ in range(8-len(unchar)):
            unchar += '0'
        sixteen = int(unchar,2)
        sixteen = hex(sixteen)
        sixteen = sixteen[2:]
        if len(sixteen) == 1:
            sixteen = '0' + sixteen
        h.write(sixteen + ' ')

f.close()
h.close()