import boto3
import json
import requests
import time
from string import rstrip
from random import randint


now = time.localtime()
date = ""
date = date + str(now.tm_year)+ "-" + str(now.tm_mon) + "-" + str(now.tm_mday)
time = ""
time = time + str(now.tm_hour)+ ":" + str(now.tm_min) + ":" + str(now.tm_sec)
print(date, time)
url = "http://i3a211.p.ssafy.io:8399/ssafy/api/violation"
#f = open('/home/pi/Desktop/programs/cases.txt', 'r')
line = randint(1,100000)
gps_data = open('/home/pi/Desktop/programs/gpsdata.txt','r')
gps_lat = gps_data.readline().rstrip()
gps_lng = gps_data.readline()
print(gps_lat, gps_lng)
r = requests.post(url, json = {
    "userNo": 2,
    "lat": gps_lat,
    "lng": gps_lng,
    "date": date,
    "time": time,
    "videoUrl": 'http://d1xevv8xa9hsha.cloudfront.net/' + str(line) + '.mp4',
    "report_status": 0,
    "item": "",
    "carNum": "",
    "spot": "",
    "contents": "",
})

print("status code:", r.status_code)


s3 = boto3.client('s3')


filename = 'output.mp4'


bucket_name = 'pleasedontbechargebomb'
newname = '{}.mp4'.format(line)
print(line)
print(newname)
#f.close()
gps_data.close()
s3.upload_file(filename, bucket_name, newname)
print('complete')
