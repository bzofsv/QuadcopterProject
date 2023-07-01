#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(pose):
    pub = rospy.Publisher('velocities', String, queue_size=10) 
    pub2 = rospy.Publisher('input', String, queue_size=10)
    #TODO: MAKE ORB SLAM'S THING KEEP SEDING A CHECKER TO MY HOVER CODE, IF CHECKER IS NOT RECIEVED THEN MAINTAIN ALTITUDE
    k = 1.0
    target = 1.0
    bruh = str(pose).split()
    pose = bruh[1]
    pose = pose[1:]
    pose = pose[:-1]
    poo = float(pose)
    vel = k * (target + poo)
    rospy.loginfo(vel)
    pub.publish(str(vel))
    pub2.publish("FL~" + str(vel) + ' ')
    pub2.publish("FR~" + str(vel) + ' ')
    pub2.publish("BL~" + str(vel) + ' ')
    pub2.publish("BR~" + str(vel) + ' ')
    
def init():
    rospy.loginfo("started")
    rospy.init_node('flight', anonymous=True)
    rospy.Subscriber('/pose', String, callback)
    
    rospy.spin()
if __name__ == '__main__':
    init()
