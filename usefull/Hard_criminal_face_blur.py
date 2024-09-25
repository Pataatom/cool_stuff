import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    raise IOError("Failed to open the camera")

while True:
    total_count = 0
    ret, frame = stream.read()
    if not ret:
        raise IOError("I don't know, something failed")

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # smaller minNeighbors the more sensitive it is to "faces"
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30))
    faces_count = 0
    for (x, y, w, h) in faces:
        faces_count += 1
        #cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
        if faces_count == 1:
            face_range_x = (x, w) #this needs to be think thru to work, but the bb_x should be in this range
            black_box_x = x
            black_box_width = w
    eyes = eye_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=4, minSize=(25, 25), maxSize=(30, 30))
    eyes_count = 0
    for (x, y, w, h) in eyes:
        eyes_count += 1
        #cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
        black_box_y = y
        black_box_height = h
        if eyes_count == 2 and y < black_box_y:
            head_tilt_compensation = y
    try:
        cv2.rectangle(frame, (black_box_x, black_box_y - 10), (black_box_x + black_box_width, black_box_y + black_box_height
                                                          + 10), (0, 0, 0), -1)
    except NameError:
        pass
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
stream.release()
cv2.destroyAllWindows()