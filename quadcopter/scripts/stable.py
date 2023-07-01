#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu

prevY = 0.0
aY = 0.0
currV = 0.0

def callback(data):
    
    bruh = str(data).split()
    data = bruh[1]
    data = data[1:]
    data = data[:-1]
    
    pub = rospy.Publisher('steadyV', String, queue_size=10)
    pub2 = rospy.Publisher('input', String, queue_size=10)
    target = 1.0
    i = 0.03
    j = 0.1
    k = 0.2
    global aY
    global prevY
    global currV
    
    y = float(data)
    if y - prevY < i and y + target < j:
        pub.publish(str(currV))
        pub2.publish("FL~" + str(currV) + ' ')
        pub2.publish("FR~" + str(currV) + ' ')
        pub2.publish("BL~" + str(currV) + ' ')
        pub2.publish("BR~" + str(currV) + ' ')
        #pub.publish(str(prevY) + 'asdf' + str(y - prevY) + str(y + target))
    prevY = y
        
        
        
def callback2(Imu):
    global aY
    aY = Imu.linear_acceleration.y
    
def callback3(String):
    bruh = str(String).split()
    String = bruh[1]
    String = String[1:]
    String = String[:-1]
    
    global currV
    
    currV = float(String)
    
def init():
    rospy.init_node('stableV', anonymous=True)
    rospy.Subscriber('/pose', String, callback)
    rospy.Subscriber('/camera/imu', Imu, callback2)
    rospy.Subscriber('velocities', String, callback3)
    
    rospy.spin()
    
if __name__ == '__main__':
    init()
