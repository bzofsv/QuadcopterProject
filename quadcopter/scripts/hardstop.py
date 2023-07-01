#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
    
def init():
    rospy.init_node('hardstopped', anonymous=False)
    pub = rospy.Publisher('input', String, queue_size=10)
    
    while not rospy.is_shutdown():
        pub.publish("FL~" + str(0.0) + ' ')
        pub.publish("FR~" + str(0.0) + ' ')
        pub.publish("BL~" + str(0.0) + ' ')
        pub.publish("BR~" + str(0.0) + ' ')
    
    rospy.spin()
if __name__ == '__main__':
    init()
