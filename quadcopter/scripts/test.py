#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu

def init():
    rospy.init_node('stableV', anonymous=True)
    pub = rospy.Publisher('/pose', String, queue_size=10)
    
    while True:
        pub.publish(input('poooooooooo \n'))
    
    rospy.spin()
    
    
if __name__ == '__main__':
    init()
