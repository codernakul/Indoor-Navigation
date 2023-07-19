#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
#from turtlesim.msg import Pose
#mport math




def talker():
    global pub,rate,cmd
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
   
    rospy.init_node("turtle_spiral" ,anonymous=True)
    rospy.loginfo("node is published")
    rate = rospy.Rate(10)
    #set the loop rate
    #keep publishing until a Ctrl-C is pressed
    cmd=Twist()
    spiral_move()




def spiral_move():
    global pub,cmd
    i=0
    cmd.linear.x=i


    while not rospy.is_shutdown():
     
     
        #(float(input("enter angular vel")))
    
       # while i<10.0:
       cmd.linear.x=i
       cmd.angular.z=2
       pub.publish(cmd)
          
       i=i+0.01
       rate.sleep()
        
    cmd.linear.x=0
    cmd.angular.y=0
    pub.publish(cmd)






if __name__ == '__main__':
                     talker()
    
