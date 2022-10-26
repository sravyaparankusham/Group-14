import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
#this code is used to call out all the names from the data
path = 'attimage'
images =[]
classNames = []
mylist = os.listdir(path)
print(mylist)

#import the img one by one
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) #this line to split thetext and show the first word
print(classNames)

#ENCODING PROCESS:

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #img converted to rGb
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readline()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')





encodeListKnown = findEncodings(images)
#print(len(encodeListKnown))
print("Encoding completed")

#initialize the wecam

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    #find location to avoid multiplr faces and encode into it
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    #finding the matches:
    for encodeFace,faceloc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis) #find the lowest and find the persom

        #display bounding box and name
        if matches[matchIndex]:
            pn = classNames[matchIndex].upper()
           # print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 =  y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,pn,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(pn)



    cv2.imshow('Webcam',img)
    cv2.waitKey(1)











