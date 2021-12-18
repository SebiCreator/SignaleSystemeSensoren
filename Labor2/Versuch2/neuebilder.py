import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
#cap.set(17, 0)
#cap.set(15, 10)
cap.set(14, 12)
cap.set(15, 0)
print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))

counter = 0
gray = 0

while (counter < 10):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    cv2.imwrite(f"Bilder/Weissbild{counter}.png", gray)
    counter += 1
    time.sleep(0.5)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break;

cap.release()
cv2.destroyAllWindows()
print(np.array(gray).shape)
print(gray)