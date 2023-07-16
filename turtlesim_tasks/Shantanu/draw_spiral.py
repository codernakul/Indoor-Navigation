#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist
from rosgraph_msgs.msg import Log

end = False
spd = 1

def msg_callback(msg: Log):
    global end
    if msg.level == 4:
        end = True      

if __name__ == '__main__':

    rospy.init_node('turtle_controller')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    sub = rospy.Subscriber('/rosout', Log, callback = msg_callback)
    rate = rospy.Rate(10)

    while not end:
        cmd = Twist()
        cmd.linear.x = spd
        cmd.angular.z = math.pi
        pub.publish(cmd)
        spd += 0.1
        rate.sleep()