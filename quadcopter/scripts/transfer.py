#!/usr/bin/env python3

#transfers the data from raspberry pi to the Arduino flight controller
import rospy
import serial
from std_msgs.msg import String


def callback(String):
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    String = str(String).split(' ', 1)[1]
    ser.write(bytes(String, 'utf-8'))
    
def init():
   rospy.init_node('transfer', anonymous=True)
   rospy.Subscriber('input', String, callback)
   
   rospy.spin()
    
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    init()
