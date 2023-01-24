import cv2
#dootlinux
#cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,150)

def findC(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOUR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("video",mask)
    
while False:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(40)==27:
        break

 
capture = cv2.VideoCapture(0)
 
while (True):
 
    (ret, frame) = capture.read()
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 190, 255, cv2.THRESH_BINARY)
 
 
    cv2.imshow('video bw', blackAndWhiteFrame)
    cv2.imshow('video original', frame)
 
    if cv2.waitKey(1) == 27:
        break
 
capture.release()
cv2.destroyAllWindows()
