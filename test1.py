import cv2 as c 

img = c.imread("ferrari.jpg")
c.imshow("Image",img)

c.waitKey(0)

c.destroyAllWindows()
