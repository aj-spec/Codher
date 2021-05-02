import cv2
import sqlite3
import numpy as np

faceDetect = cv2.CascadeClassifier('C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\haarcascade_frontalface_default.xml')

rec = cv2.face.LBPHFaceRecognizer_create()
cam = cv2.VideoCapture(0)
rec.read("C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\recognize\\trained.yml")


def getProfile(id):
	conn = sqlite3.connect("C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\faceDetection.db")
	sql = "select * from people where id="+str(id)
	ResultSet = conn.execute(sql)
	profile = None

	for row in ResultSet:
		profile = row
	return profile

id = 0
#adding a label
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
	ret,frame = cam.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray,1.3,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h+30),(0,0,255),2)
		id,conf = rec.predict(gray[y:y+h,x:x+w])
		profile = getProfile(id)
		if profile != None:
			cv2.putText(frame,str(profile[1]),(x,y+h),font,0.90,(0,0,255),2)
			cv2.putText(frame,str(profile[2]),(x,y+h+20),font,0.90,(0,0,255),2)
	cv2.imshow('Faces',frame)
	
	if cv2.waitKey(1) == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()
		