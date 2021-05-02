import cv2
import os
import numpy as np
from PIL import Image

# for trainer we are using the algorithm - LBPH [Local Binary Pattern Histogram]
recognizer=cv2.face.LBPHFaceRecognizer_create()

path = "C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\DATASET"

def getImagesWithID(path):
	#this will give the paths of all the images in the os directory DATASET
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	faces= []
	IDs = []

	for imagePath in imagePaths:
		#here we are opening the image one by one and converting into grayscale
		faceImg = Image.open(imagePath).convert('L')
		#convert into numpy array
		faceNp = np.array(faceImg,'uint8')
		#getting the face ID from the imagePath
		ID = int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		print(ID) # for verifying that the image is trained

		IDs.append(ID)
		#open that image
		cv2.imshow("Training",faceNp)
		cv2.waitKey(10)

	return np.array(IDs),faces

Ids,faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save("C:\\Users\\Charu Anant Rajput\\Desktop\\FaceRecognition\\recognize\\trained.yml")
cv2.destroyAllWindows()