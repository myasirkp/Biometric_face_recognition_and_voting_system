import cv2, os
import numpy as np
from PIL import Image

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
