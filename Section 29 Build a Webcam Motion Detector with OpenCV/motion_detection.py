# Motion detection must be triggered on a static background i.e no moving objects when program is initiated
# FIXME: This script does not seem to record more than one entry. Compare with the file from the lecture 
# https://render.githubusercontent.com/view/ipynb?color_mode=dark&commit=836574eeb29b4fbb6192c9e8ade6f63facac6858&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f617264697473756c63657465616368696e672f746865707974686f6e6d656761636f757273652f383336353734656562323962346662623631393263396538616465366636336661636163363835382f5331362d4170702d362d4275696c642d612d57656263616d2d4d6f74696f6e2d4465746563746f722e6970796e62&nwo=arditsulceteaching%2Fthepythonmegacourse&path=S16-App-6-Build-a-Webcam-Motion-Detector.ipynb&repository_id=146125948&repository_type=Repository
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
