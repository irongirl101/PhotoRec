import cv2 as c 

cap = c.VideoCapture(0)#0-> 1 webcam, 1-> 2 webcams etc etc 

while True: #loop for frames 
    ret,frame = cap.read() # ret is a bool as to whether a frame was read successfully or not , frame is a numpy array ffo the image captured 
    if not ret: 
        break
    c.imshow("image",frame) # shows frame 

    if c.waitKey(1) and 0xFF == "q":  #wait till a key is pressed in order to exit 
        break

cap.release() #close the camera 
c.destroyAllWindows() #close the windows 
