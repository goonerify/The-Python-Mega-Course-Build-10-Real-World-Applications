# Motion detection must be triggered on a static background i.e no moving objects when program is initiated
from datetime import datetime, time

import cv2
import pandas

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Removes noise and increases accuracy of the image
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    # Classify as white (motion) or black (no motion)
    thresh_frame = cv2.threshold(delta_frame, 30, 25, cv2.THRESH_BINARY)[1]

    # Smooth threshold frame (Remove black holes from white areas in the image)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        # ignore contour if area < 10000px (100px X 100px window)
        if cv2.contourArea(contour) < 10000: # Adjustable area of capture
            continue
            
        status = 1

        (x,y,w,h) = cv2.boundingRect(contour)
        # Use the bounds to draw a green rectangle in the current frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)
    # Record when an object enters or exits a frame
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(gray)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
