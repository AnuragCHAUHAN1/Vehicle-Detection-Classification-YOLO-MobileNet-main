""""""
# Import necessary libraries
import cv2

var = cv2.__version__
    

carVideo = cv2.VideoCapture('test/assignment-clip.mp4')


cars_cascade = cv2.CascadeClassifier('test/cars.xml')

def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 255, 0), thickness=2)
    return frame

while carVideo.isOpened():
    ret, frame = carVideo.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    else :        
        cars_frame = detect_cars(frame)
        cv2.imshow('frame', cars_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


carVideo.release()
cv2.destroyAllWindows()
