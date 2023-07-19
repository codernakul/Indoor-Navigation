
import rospy
from geometry_msgs.msg import Twist
#from turtlesim.msg import Pose

def talker():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    #we need to initialize the node
    
   
    rospy.init_node("turtle_circle" ,anonymous=True)
    rospy.loginfo("node is published")
    #set the loop rate
    rate = rospy.Rate(2) # 2hz
  
    
    while not rospy.is_shutdown():
        msg=Twist()
        msg.angular.z=4.0
        #(float(input("enter angular vel")))
        #i=0
        #while i<5:
        msg.linear.x=10.0
        #(float(input("enter linear vel")))
        '''msg.linear.y=3.0 
        msg.linear.x=-3.0
        msg.linear.y=-3.0 
               #i=i+1'''
        pub.publish(msg)
        rospy.sleep(0.5)
        



        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
