import cv2
import sys
import numpy
import os
from datetime import datetime
import csv
import excel_entry as ex




haar_file = 'haarcascade\\haarcascade_frontalface_default.xml'
datasets = 'datasets'

print('Initiating face recognization-')

# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(
        datasets):  # OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames)
    for subdir in dirs:
        names[id] = subdir  # inserting first file name inside the name[]
        subjectpath = os.path.join(datasets,
                                   subdir)  # os.path.join() method in Python join one or more path components intelligently.
        for filename in os.listdir(
                subjectpath):  # os.listdir(subjectpath) is used to extract all the files and directorys specified in the path shared as parameter
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))  # inserting the file containg the
            lables.append(int(lable))  # keeping count of appends
        id += 1  # acting as index for name  list
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]  # creat array of images and labels and stores them
model = cv2.face.LBPHFaceRecognizer_create()  # Algorithm to detect faces. It labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number
model.train(images, lables)

# Part 2: Use fisherRecognizer on camera stream
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)  # to capture form webcam
while True:
    (_,
     im) = webcam.read()  # it reads the frame passed and store them in im and _ stores true or false if the frame passed or not
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        # Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if prediction[1] < 500:

            cv2.putText(im, '% s ' % (names[prediction[0]]), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            name = names[prediction[0]]
            ex.make_attendance_entry(name)
        else:
            cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    cv2.imshow('OpenCV', im)

    key = cv2.waitKey(10)
    if key == 27:
        break
