import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  
  #cv2.imshow('webcam feed' , frame)
  print(frame)
  x,y,z = cv.detect_common_objects(frame)
  output_img = draw_bbox(frame, x,y,z)
  print(y)
  cv2.imshow("Object_detect",output_img)
  if cv2.waitKey(1) & 0xFF == ord(' '):
    break
    
cap.release()
cv2.destroyAllWindows()
