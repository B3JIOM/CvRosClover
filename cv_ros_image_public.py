import numpy as py
import cv2 as cv
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('png')
image_pub = rospy.Publisher('~debug', Image)

bridge = CvBridge()

def image_callback(data):
    img = cv.imread('shapes.png')
    image_pub.publish(bridge.cv2_to_imgmsg(img, 'bgr8'))
    
    print(".") 

image_sub = rospy.Subscriber('/main_camera/image_raw', Image, image_callback)
rospy.spin()