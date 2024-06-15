import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while (True):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        print('no frame')
        break

cap.release()
cv2.destroyAllWindows()
