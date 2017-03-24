import cv2, os
import numpy as np
from PIL import Image
import sys
import csv
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(5,GPIO.OUT)

GPIO.output(5,0)

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('recognize.xml')

cascadePath = '/root/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
path1='./detect'
image_paths = [os.path.join(path1, f) for f in os.listdir(path1)]
for image_path in image_paths:
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    for (x, y, w, h) in faces:
        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        print "Identified as {} with confidence {}".format(nbr_predicted, conf)
        cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
        cv2.waitKey(1000)
with open('table.csv','rb') as csvfile:
    read=csv.reader(csvfile)
    idnums=[]
    names=[]
    statuses=[]
    row_num=0
    for row in read:
        idnum= row[0]
        name=row[1]
        status=row[2]
        idnums.append(idnum)
        names.append(name)
        statuses.append(status)
        row_num=row_num+1
data=nbr_predicted
data=str(data)
find_id=idnums.index(data)
find_name=names[find_id]
print find_name
if int(statuses[find_id])==0:
    statuses[find_id]=1
    print 'Ready to vote'
    GPIO.output(5,1)
    GPIO.wait_for_edge(3,GPIO.FALLING,bouncetime=300)
    GPIO.output(5,0)
    print 'Vote casted'
    row_write=[]
    with open('table.csv','wb') as csvfile:
        write=csv.writer(csvfile)
        for i in range(0,row_num):
            row_write=idnums[i],names[i],statuses[i]
            write.writerow(row_write)
else:
    print 'already voted'

