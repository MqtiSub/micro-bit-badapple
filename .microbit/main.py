from microbit import *
from ssd1306 import initialize, clear_oled, draw_screen
from ssd1306_px import set_px

line_offset, frame_num = 0,0
initialize()
clear_oled()
f = open('record.txt',mode='r')
while True:
    line = f.readline()
    if line == 'finish!!':
        print('succeed')
        break
    dot_offset = 0
    frame_num += 1
    for dot in line:
        if dot == '':
            line_offset = -1
            draw_screen()
            sleep(100)
            print('frame:'+str(frame_num))
            break
        if dot == 0:
            set_px(dot_offset,line_offset,1)
        if dot == 1:
            set_px(dot_offset,line_offset,0)
        dot_offset += 1
    line_offset += 1
f.close()
