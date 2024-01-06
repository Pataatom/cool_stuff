import cv2

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise IOError("Can't open camera")

while True:
    ret, frame = cam.read()

    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    peoples = body_cascade.detectMultiScale(grey_frame, scaleFactor=1.3, minNeighbors=0, minSize=(30, 30))
    for (x, y, w, h) in peoples:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if not ret:
        raise IOError("Trouble capturing frame")
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()