#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV libraryimport os   
import numpy as np
import array
import os   


def publish_message():
 
  # Node is publishing to the video_frames topic using 
  # the message type Image
  pub = rospy.Publisher('video_frames', Image, queue_size=10)
     
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name.
  rospy.init_node('video_pub_py', anonymous=True)
     
  # Go through the loop 10 times per second
  rate = rospy.Rate(1) # 10hz
    
  # Create a VideoCapture object
  # The argument '0' gets the default webcam.
  cap = cv2.VideoCapture(0)  
  # Used to convert between ROS and OpenCV images
  br = CvBridge()

 
  # While ROS is still running.
  while not rospy.is_shutdown():
      Imagemainfolder = 'images'
      count = 1 
      frameRate = 1
      sec = 0
      # Capture frame-by-frame
      # This method returns True/False as well
      # as the video frame.
      while True:
        cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        ret, frame = cap.read()
        if ret == True:
          rospy.loginfo('publishing video frame')
          b = cv2.resize(frame,(426,240),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
          c = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
          # imagepath = 'Home/vihaan_rover/src/cv_basics/src/'+Imagemainfolder
          # capt = cv2.imwrite(os.path.join(imagepath,'image'+str(count)+'.jpg'), c)
          pub.publish(br.cv2_to_imgmsg(c,"bgr8"))
        else:
          break
          cap.release()
        count = count + 1
        sec = sec + frameRate
        sec = round(sec,2)
         #//it will capture image in each 0.5 second 
        # Print debugging information to the terminal
        
             
        # Publish the image.
        # The 'cv2_to_imgmsg' method converts an OpenCV
        # image to a ROS image message
             
      # Sleep just enough to maintain the desired rate
      cv2.destroyAllWindows()
      rate.sleep()
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass
