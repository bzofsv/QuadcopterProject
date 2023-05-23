#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy

def axes(Joy):
    arr = Joy.axes()
    with open('/dev/rfcomm0','w',1) as f:
        f.write('axes')
        f.write(arr)
        
def buttons(Joy):
    arr = Joy.buttons()
    with open('/dev/rfcomm0','w',1) as f:
     f.write('buttons')
     f.write(arr)
    
def send_init():
    rospy.Subscriber('joy', Joy, axes)
    rospy.Subscriber('joy', Joy, buttons)

if __name__ == '__main__':
    send_init()

