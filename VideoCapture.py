import cv2 as c 

cap = c.VideoCapture(0)

while True: 
    ret,frame = cap.read()
    if not ret: 
        break
    c.imshow("image",frame)

    if c.waitKey(0) and 0xFF == "q": 
        break

cap.release()
c.destroyAllWindows()
