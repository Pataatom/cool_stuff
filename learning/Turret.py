import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
stream = cv2.VideoCapture(0)
if not stream.isOpened():
    raise IOError("Failed to open the camera")

while True:
    # ____CAMERA____
    ret, frame = stream.read()
    if not ret:
        raise IOError("I don't know, something failed")
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # smaller minNeighbors the more sensitive it is to "faces"
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
        try:
            cv2.circle(frame, center=(x+w/2, y+h/2), color=(255,255,255), thickness=2, radius=5)
        except:
            pass
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    # ____CAMERA____

stream.release()
cv2.destroyAllWindows()