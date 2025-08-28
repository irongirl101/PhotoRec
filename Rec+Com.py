import cv2 as c
import os 

name = 'person_1'
DATASET = 'Dataset'
person_path = os.path.join(DATASET, name)

os.makedirs(person_path,exist_ok=True)
face_cascade = c.CascadeClassifier(c.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = c.VideoCapture(0)

count = 0 

while True: #loop for frames 
    ret,frame = cap.read() # ret is a bool as to whether a frame was read successfully or not , frame is a numpy array ffo the image captured 
    if not ret: 
        break
    #changing to  grayscale 
    gray = c.cvtColor(frame,c.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,minSize=(30,30),minNeighbors=5,scaleFactor=1.1)

    for(x,y,w,h) in faces: 
        c.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    frame = c.flip(frame,1)

    c.imshow("Face Detect",frame)

    if c.waitKey(1) and 0xFF == "q":  #wait till a key is pressed in order to exit 
        break

cap.release() #close the camera 
c.destroyAllWindows() #close the windows 
