import cv2
confidence_threshold = 0.5  # if the confidence of the prediction is lower than this the prediction won't count
count_of_bbox = 0


caffe_model = r"MobileNetSSD_deploy.caffemodel"
prototxt = r"MobileNetSSD_deploy.prototxt"
# for some reason needs to be relative

try:
    # read a network model (pre-trained) stored in Caffe framework's format
    net = cv2.dnn.readNetFromCaffe(prototxt, caffe_model)
except:
    raise IOError("Can't find needed files of a model")

# dictionary with the object class id and names on which the model is trained
classNames = {0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'KOKOT', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        raise IOError("Cam not recording")

    width = frame.shape[1]
    height = frame.shape[0]
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1 / 127.5, size=(300, 300), mean=(127.5, 127.5, 127.5), swapRB=True,
                                 crop=False)
    net.setInput(blob)
    detections = net.forward()

    # detections array is in the format 1,1,N,7, where N is the detected bounding boxes
    # for each detection, the description contains : [image_id, label, conf, x_min, y_min, x_max, y_max]
    for i in range(detections.shape[2]):  # detections.shape[2] contains the max  num of detected bbox in frame
        confidence = detections[0, 0, i, 2]  # number 2 is the selector of which info from detection you want to access
        if confidence > confidence_threshold:

            count_of_bbox += 1
            class_id = int(detections[0, 0, i, 1])

            # scale to the frame
            x_top_left = int(detections[0, 0, i, 3] * width)
            y_top_left = int(detections[0, 0, i, 4] * height)
            x_bottom_right = int(detections[0, 0, i, 5] * width)
            y_bottom_right = int(detections[0, 0, i, 6] * height)

            # draw bbox around the detected object
            cv2.rectangle(frame, (x_top_left, y_top_left), (x_bottom_right, y_bottom_right), (0, 255, 0), 2)

            if class_id in classNames:
                label = classNames[class_id] + ": " + str(int(confidence*100)) + "%"

                # get width and text of the label string
                (w, h), t = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                # y_top_left = max(y_top_left, h) # don't understand this line fully, have to play with it

                # draw bounding box around the text (OPTIONAL)
                cv2.rectangle(frame, (x_top_left, y_top_left - h),
                                   (x_top_left + w, y_top_left + t), (0, 0, 0), cv2.FILLED)
                cv2.putText(frame, label, (x_top_left, y_top_left),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # fucking showing you what I got
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) >= 0:  # break with any key I suppose
        break

cap.release()
cv2.destroyAllWindows()
