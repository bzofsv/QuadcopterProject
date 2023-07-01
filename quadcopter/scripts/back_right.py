#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
    
def init():
    rospy.init_node('back_right', anonymous=False)
    pub = rospy.Publisher('input', String, queue_size=10)
    
    while not rospy.is_shutdown(): pub.publish("BL~" + str(0.5) +  " ")
    
if __name__ == '__main__':
    init()