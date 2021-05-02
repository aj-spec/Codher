import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\haarcascade_frontalface_default.xml')

def insertOrUpdate(id,name,gender):
	con = sqlite3.connect("C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\faceDetection.db")
	sql = "Select * from people5 where id="+str(id)
	resultSet = con.execute(sql)
	isRecordExists = 0

	for row in resultSet:
		isRecordExists = 1
	if isRecordExists == 1:
		sql = "update people5 set name="+str(name)+" and gender="+str(gender)+" where id="+str(id)
	else:
		sql = "insert into people5 (id,name,gender) values ("+str(id)+","+str(name)+","+str(gender)+")"

	con.execute(sql)
	con.commit()
	con.close()



#taking input from the user
id = input("Enter ID:")
name = input("Enter name:")
gender = input("Gender (MALE/FEMALE):")
insertOrUpdate(id,name,gender)

#opening the webcam
cam = cv2.VideoCapture(0)

sampleNumber = 0

while True:
	ret,frame = cam.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray,1.3,5)

	for(x,y,w,h) in faces:
		sampleNumber+=1
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.imwrite("C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\DATASET\\User."+str(id)+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
	cv2.imshow('Faces',frame)
	cv2.waitKey(100)
	if sampleNumber == 20:
		cam.release()
		cv2.destroyAllWindows()
		break