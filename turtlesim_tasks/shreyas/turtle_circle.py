
import rospy
from geometry_msgs.msg import Twist
#from turtlesim.msg import Pose

def talker():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node("turtle_circle" ,anonymous=True)
    rospy.loginfo("node is published")
    #set the loop rate
    rate = rospy.Rate(2) # 2hz
    #keep publishing until a Ctrl-C is pressed
    
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
        rate.sleep()



        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
