import cv2
from curses import wrapper

stream = cv2.VideoCapture(0)
if not stream.isOpened():
    raise IOError("Can't open camera")
while  True:
    ret, frame = stream.read()
    if not ret:
        raise IOError("No more camera for today")

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

stream.release()
cv2.destroyAllWindows()