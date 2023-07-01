#!/usr/bin/env python3

import rospy
import time
from sensor_msgs.msg import Imu
from std_msgs.msg import String
from nav_msgs.msg import Odometry

prevY = 0.0
prevA = 0.0
prevU = 0.0
t1 = 0.0

currY = 0.0

def callback(Odometry):
    pub = rospy.Publisher('/pose', String, queue_size=10)
    y = Odometry.pose.pose.position.y
    global currY
    currY = y #update the y with more accurate data
    
    global prevY
    prevY = y
    
    rospy.loginfo(str(currY) + 'good!~~~~~~~~~~~~~~~~~~~~~~~~')
    pub.publish(str(currY) + "")
    
    
def callback2(Imu):
    
    data = Imu.linear_acceleration
    y = data.y
    c = 0.3
    global prevA
    a = prevA * c + y * (1 - c)
    prevA = a
    
    global t1
    global prevU
    global prevY
    
    a += 9.80665
    
    dt = time.time() - t1
    t1 = time.time()
    u = prevU + a * dt
    #rospy.loginfo(((a + prevA) / 2) * dt)
    prevU = u
    #rospy.loginfo(u)
    y = prevY + u * dt
    global currY
    currY = y
    
    prevY = y
    
    # rospy.loginfo(str(currY) + 'bad')
    
    # pub = rospy.Publisher('/pose', String, queue_size=10)
    # pub.publish(str(currY) + "")
    
def poseInit():
    rospy.loginfo("started")
    rospy.init_node('orbslam_data', anonymous=True)
    rospy.Subscriber('/camera/imu', Imu, callback2)
    rospy.Subscriber('/orb_slam/odom', Odometry, callback)
    
    rospy.spin()
if __name__ == '__main__':
    t1 = time.time()
    poseInit()
