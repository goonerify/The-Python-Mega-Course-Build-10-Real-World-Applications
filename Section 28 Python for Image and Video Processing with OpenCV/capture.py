import time

import cv2

# Capture video from webcam
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('Auntie.Edna.mp4')

# Used to capture number of frames per second
frames = 0

while True:
    frames = frames + 1

    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(10)

    # Get the unicode value with ord
    if key == ord('q'):
        print(key)
        break
    
print(frames)
video.release()
cv2.destroyAllWindows()

# video.release()
