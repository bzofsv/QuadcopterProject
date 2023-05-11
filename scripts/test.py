#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy

def callback(Joy):
    rospy.loginfo(rospy.get_caller_id() + 'pog! %s', Joy.axes)
    rospy.loginfo(rospy.get_caller_id() + 'pog! %s', Joy.buttons)

def joystick_init():
    rospy.init_node('joystick', anonymous=True)
    rospy.Subscriber('joy', Joy , callback)
    
    rospy.spin()

if __name__ == '__main__':
    joystick_init()    
        
