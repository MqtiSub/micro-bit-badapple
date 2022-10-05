import cv2
import sys

filepath = './badapple.avi'
video = cv2.VideoCapture(filepath)
if not video.isOpened():
    print("Could not open video")
    sys.exit()
ok, frame = video.read()
if not ok:
    print('Cannot read video file')
    sys.exit()
succeed  = False
num = 0

while True:
    f = open('./record.txt',mode='a')
    ok,frame = video.read()
    succeed = True
    num += 1
    if(ok):
        img = cv2.resize(frame,(86,64))
        for line in img:
            for dot in line:
                if dot[0] >= 130:
                    color = 0
                else:
                    color = 1
                f.write(str(color))
            f.write('\n')
        f.write('\n')
        f.close()
        print(f'frame:{num}')

    else:
        if succeed == True:
            with open('./record.txt',mode='a') as f:
                f.write('finish!!')
            print('worked good')
        else:
            print('error')
        break