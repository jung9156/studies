import picamera
from time import sleep


camera = picamera.PiCamera()
camera.rotation = 180
i = 0
while True:
    i = i % 6

    camera.start_recording('sample{}.h264'.format(i))
    sleep(5)
    camera.stop_recording()

    text = open('/home/pi/Desktop/programs/input.txt','w')
    print 'start'
    if i == 0:
        data = ("file 'sample3.mp4'\n")
        text.write(data)
        data = ("file 'sample4.mp4'\n")
        text.write(data)
        data = ("file 'sample5.mp4'\n")
        text.write(data)
        data = ("file 'sample0.mp4'\n")
        text.write(data)
        print '0'
    if i == 1:
        data = ("file 'sample4.mp4'\n")
        text.write(data)
        data = ("file 'sample5.mp4'\n")
        text.write(data)
        data = ("file 'sample0.mp4'\n")
        text.write(data)
        data = ("file 'sample1.mp4'\n")
        text.write(data)
        print '1'
    if i == 2:
        data = ("file 'sample5.mp4'\n")
        text.write(data)
        data = ("file 'sample0.mp4'\n")
        text.write(data)
        data = ("file 'sample1.mp4'\n")
        text.write(data)
        data = ("file 'sample2.mp4'\n")
        text.write(data)
        print '2'
    if i == 3:
        data = ("file 'sample0.mp4'\n")
        text.write(data)
        data = ("file 'sample1.mp4'\n")
        text.write(data)
        data = ("file 'sample2.mp4'\n")
        text.write(data)
        data = ("file 'sample3.mp4'\n")
        text.write(data)
        print '3'
    if i == 4:
        data = ("file 'sample1.mp4'\n")
        text.write(data)
        data = ("file 'sample2.mp4'\n")
        text.write(data)
        data = ("file 'sample3.mp4'\n")
        text.write(data)
        data = ("file 'sample4.mp4'\n")
        text.write(data)
        print '4'
    if i == 5:
        data = ("file 'sample2.mp4'\n")
        text.write(data)
        data = ("file 'sample3.mp4'\n")
        text.write(data)
        data = ("file 'sample4.mp4'\n")
        text.write(data)
        data = ("file 'sample5.mp4'\n")
        text.write(data)
        print '5'

    text.close()
    i += 1
