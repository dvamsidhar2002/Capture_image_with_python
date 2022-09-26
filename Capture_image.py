from ast import main
from threading import main_thread
import cv2
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

def takePicture():
    
    (grabbed, frame) = cap.read()
    showimg = frame
    cv2.imshow('img1', showimg)  # display the captured image
    cv2.waitKey(1)
    time.sleep(0.3) # Wait 300 miliseconds
    image = 'D:\Python programs\photo.png'
    cv2.imwrite(image, frame)
    cap.release()
    return image

if __name__ == "__main__":
    takePicture()