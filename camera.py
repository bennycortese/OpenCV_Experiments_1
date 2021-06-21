import cv2


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

    def return_cap(self):
        return self.cap
