#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

prevX = 0.0
prevY = 0.0
prevZ = 0.0

def callback(Imu):
    data = Imu.linear_acceleration
    x = data.x
    y = data.y
    z = data.z
    c = 0.9
    global prevX
    global prevY
    global prevZ
    newX = prevX * c + x * (1 - c)
    newY = prevY * c + y * (1 - c)
    newZ = prevZ * c + z * (1 - c)
    prevX = newX
    prevY = newY
    prevZ = newZ
    
    rospy.loginfo('x: ' + str(newX))
    rospy.loginfo('y: ' + str(newY))
    rospy.loginfo('z: ' + str(newZ))
    
def lpInit():
    rospy.loginfo("started")
    rospy.init_node('lpFilter', anonymous=True)
    rospy.Subscriber('/camera/imu', Imu, callback)
    
    rospy.spin()
if __name__ == '__main__':
    lpInit()
