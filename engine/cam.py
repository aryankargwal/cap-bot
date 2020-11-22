import os
import time 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
i=0  

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    path="./images/"
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
    cv2.imwrite(path+str(i)+'.jpg',frame)
    i+=1
    time.sleep(5)
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
