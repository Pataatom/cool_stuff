import cv2
from curses import wrapper

stream = cv2.VideoCapture(0)
if not stream.isOpened():
    raise IOError("Can't open camera")
while True:
    ret, frame = stream.read()  # ret == return
    if not ret:
        raise IOError("No more camera for today")

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):  # ord() cast q to its integer that is associated with its ascii number
        break

stream.release()  # ending the stream
cv2.destroyAllWindows()  # ending the stream