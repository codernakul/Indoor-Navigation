import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt,atan2,pow
 
class total_move():
   
       def controller(self):
           global pub
          
           rospy.init_node('gotogoal', anonymous=True)
           pub= rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
           self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.current_pose)
   
           self.pose = Pose()
          
           self.rate=rospy.Rate(10)

         
           
           
                    
         
                    
       def current_pose(self,msg):
      
           
           self.pose = msg
           self.pose.x= round(self.pose.x, 3)
           self.pose.y = round(self.pose.y,3)
          
   
       def distance(self, target_pose):
          
           return sqrt(pow((target_pose.x - self.pose.x), 2) + pow((target_pose.y - self.pose.y), 2))
   
       def linear_vel(self, target_pose,prop_const=1.4):
           return  prop_const*self.distance(target_pose)
       
       def turning_angle(self, target_pose,):
         
           return atan2(target_pose.y - self.pose.y, target_pose.x - self.pose.x)
   
       
       def angular_vel(self, target_pose,const=4.5):
           return const*(self.turning_angle(target_pose) - self.pose.theta)
   
       

       def move_to_target(self):
           global target_pose
       
           target_pose = Pose()
   
           target_pose.x = float(input("enter the x target: "))
           target_pose.y = float(input("enter the y target: "))
   
           distance_error = float(input("enter the error: "))
   
           vel_msg = Twist()
   
           while self.distance(target_pose) >= distance_error:
   
               vel_msg.linear.x = self.linear_vel(target_pose)
              
               vel_msg.angular.x = 0
               vel_msg.angular.y = 0
               vel_msg.angular.z = self.angular_vel(target_pose)
               pub.publish(vel_msg)
               
               self.rate.sleep()
             
   
              
   
              
   
           # break
           vel_msg.linear.x = 0
           vel_msg.angular.z = 0
           pub.publish(vel_msg)
   
           
           rospy.spin()
   
if __name__ == '__main__':
              
              x = total_move()
              x.controller()
              x.move_to_target()
            