import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([110, 50, 50])
    upper_green = np.array([130, 255, 255])
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    
    cv2.imshow("Webcam", frame)
    cv2.imshow("Green Mask", green_mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()