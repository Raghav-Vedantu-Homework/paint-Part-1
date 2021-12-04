import numpy as np
import cv2
from collections import deque

blueLower = np.array([100,60,60])
blueUpper = np.array([140,255,255])

# Setup deques to store separate colors in separate arrays
#Note :Each deque will hold the pixels which has that colour
Bpoint = [deque()]
Rpoint = [deque()]
Gpoint = [deque()]
Ypoint = [deque()]
Cpoint = [deque()]
#Initialization of different parameters.
#index to Blue, red, green , yellow deque respectively
Bindex = 0 
Rindex = 0
Gindex = 0
Yindex = 0
Cindex = 0
#color
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (0, 255, 255)
RED = (0, 0, 255)
CYAN = (255, 255, 0)
colorIndex = 0
colors = [BLUE, GREEN, RED, YELLOW, CYAN]

fontName = cv2.FONT_HERSHEY_SIMPLEX

#paint inerface
paintWindow = np.zeros((471,636, 3)) +255
cv2.namedWindow("Paint", cv2.WINDOW_AUTOSIZE)

#Load the video
#Create the camera capture object, get each frame and convert to HSV.
camera = cv2.VideoCapture(0)
while True:
    # Grab the current paintWindow
    (grabbed, frame) = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Add the coloring options to the frame
    frame = cv2.rectangle(frame, (40, 1), (140,65), GRAY, -1) #Note : -1 indicates to fill the rectangle
    frame = cv2.rectangle(frame, (160, 1), (255,65), colors[0], -1)
    frame = cv2.rectangle(frame, (275, 1), (370,65), colors[1], -1)
    frame = cv2.rectangle(frame, (390, 1), (485,65), colors[2], -1)
    frame = cv2.rectangle(frame, (505, 1), (600,65), colors[3], -1)
    frame = cv2.rectangle(frame, (615, 1), (700,65), colors[4], -1)
    cv2.putText(frame, "Clear All", (49, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    cv2.putText(frame, "Blue", (185, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    cv2.putText(frame, "Green", (298, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    cv2.putText(frame, "Red", (420, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    cv2.putText(frame, "Yellow", (520, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    cv2.putText(frame, "Cyan", (640, 33), fontName, 0.5, WHITE, 2, cv2.LINE_AA)
    
    if not grabbed:
        break

    cv2.imshow("Paint",paintWindow)
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) == ord("q"):
        cv2.imwrite("yourPainting.jpg", paintWindow)
        break

camera.release()
cv2.destroyAllWindows()





