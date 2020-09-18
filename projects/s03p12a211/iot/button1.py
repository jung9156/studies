import picamera
import RPi.GPIO as GPIO
from time import sleep
import subprocess


def make_movie():

    subprocess.call('sudo rm -r sample*.mp4', shell=True)
    print('movie change')
    subprocess.call('MP4Box -fps 30 -add sample0.h264 sample0.mp4', shell=True)
    subprocess.call('MP4Box -fps 30 -add sample1.h264 sample1.mp4', shell=True)
    subprocess.call('MP4Box -fps 30 -add sample2.h264 sample2.mp4', shell=True)
    subprocess.call('MP4Box -fps 30 -add sample3.h264 sample3.mp4', shell=True)
    subprocess.call('MP4Box -fps 30 -add sample4.h264 sample4.mp4', shell=True)
    subprocess.call('MP4Box -fps 30 -add sample5.h264 sample5.mp4', shell=True)
    print 'sum movie'
    subprocess.call('ffmpeg -f concat -i input.txt -codec copy output.mp4 -y', shell=True)
    print 'send'
    subprocess.call('python Toaws.py', shell=True)
    print 'btn complete'


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
flag = 0

try:
    while True:
        inputIO = GPIO.input(18)

        if inputIO == False:
	    flag = 1

	if flag == 1:
            make_movie()
            GPIO.output(17, GPIO.HIGH)

        else:
            GPIO.output(17, GPIO.LOW)

	flag = 0


except KeyboardInterrupt:
    GPIO.cleanup()
