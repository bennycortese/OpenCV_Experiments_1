import cv2
from camera import Camera

while True:
    video_uno = Camera()
    success, img = video_uno.return_cap().read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #TODO - figure out why this is erroring