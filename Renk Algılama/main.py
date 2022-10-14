import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # blue
    lower_color = np.array([161, 155, 84])
    upper_color = np.array([179, 255, 255])
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    color = cv2.bitwise_and(frame, frame, mask = color_mask)
    cv2.imshow("Webcam", frame)
    cv2.imshow("Color", color)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()