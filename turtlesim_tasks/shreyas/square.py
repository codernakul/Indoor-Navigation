#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
PI=3.14159265
#class turtle_bot:

def angle():
    global rate
    rospy.init_node('square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rate=rospy.Rate(200)
  
     
    print("Let's rotate your robot")
    speed_a=30
    angle = 90.567
    #clockwise = input("Clockwise?: ") #True or false
    #clockwise=1

    angular_speed =(speed_a*2*PI)/360
    relative_angle = (angle*2*PI)/360

    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    
    #if clockwise:
    #vel_msg.angular.z = -abs(angular_speed)
    #else:
    vel_msg.angular.z = angular_speed
   
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
      

  
    vel_msg.angular.z = 0
    pub.publish(vel_msg)
    #rospy.spin()
    #return movey()
    return
   
    

def movex():
      global speed,distance,vel_msg,pub,rate
      rospy.init_node('square', anonymous=True)
      pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
      vel_msg = Twist()
      #rate=rospy.Rate(500)

  
      print("Let's move your robot")
      speed = float(input("Input your speed:"))
      distance = float(input("Type your distance:"))
      '''speed =2.0
      distance=3.5'''

      #isForward = input("Foward?: ")#True or False
  
      #Checking if the movement is forward or backwards
      #if(isForward):
      vel_msg.linear.x= speed
         
      #else:
         # vel_msg.linear.x = -abs(speed)
      #Since we are moving just in x-axis
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0
  
      while not rospy.is_shutdown():
  
        
          t0 = float(rospy.Time.now().to_sec())
          current_distance = 0.0
  
          while(current_distance < distance):
              #Publish the velocity
              pub.publish(vel_msg)
            
              t1=float(rospy.Time.now().to_sec())
             
              current_distance= speed*(t1-t0)
          #After the loop, stops the robot
          #if (current_distance=distance):
                   # angle()
          vel_msg.linear.x = 0
          
                    
          #Force the robot to stop
          pub.publish(vel_msg)
          return angle()
          

def movey():
      global rate
      

      rospy.init_node('square', anonymous=True)
      pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
      vel_msg = Twist()
      #rate=rospy.Rate(700)
  
      print("Let's move your robot in y")
      #speed = int(input("Input your speed:"))
      #distance = int(input("Type your distance:"))
      #isForward = input("Foward?: ")#True or False
  #here the coordinates x or y depends on the direction of face of turtle
  #if it's facing upwards then the verticle becomes x-axis
      #Checking if the movement is forward or backwards
      #if(isForward):
      vel_msg.linear.x= abs(speed)
         
      #else:
          #vel_msg.linear.y = -abs(speed)
      #Since we are moving just in x-axis
      vel_msg.linear.y= 0
      vel_msg.linear.z = 0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0
  
      #while not rospy.is_shutdown():
  
          
      t0 = rospy.Time.now().to_sec()
      current_distance = 0
  
      #Loop to move the turtle in an specified distance
      while(current_distance < distance):
          #Publish the velocity
          pub.publish(vel_msg)
          #Takes actual time to velocity calculus
          t1=rospy.Time.now().to_sec()
          #Calculates distancePoseStamped
          current_distance= speed*(t1-t0)
  
      vel_msg.linear.y = 0
          #Force the robot to stop
      pub.publish(vel_msg)
      return angle()
#def int():
      '''global vel_msg,pub
      rospy.init_node('square', anonymous=True)
      pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
      vel_msg = Twist()

      '''
      #angle()
def movex2():
     # global speed,distance,vel_msg,pub,rate
      rospy.init_node('square', anonymous=True)
      pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
      vel_msg = Twist()
      #rate=rospy.Rate(500)

  
      print("Let's move your robot in x")
      
      #distance = float(input("Type your distance:"))
      #isForward = input("Foward?: ")#True or False
  
      #Checking if the movement is forward or backwards
      #if(isForward):
      vel_msg.linear.x= speed
         
      #else:
         # vel_msg.linear.x = -abs(speed)
      #Since we are moving just in x-axis
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0
  
      while not rospy.is_shutdown():
  
        
          t0 = float(rospy.Time.now().to_sec())
          current_distance = 0.0
  
          while(current_distance < distance):
              #Publish the velocity
              pub.publish(vel_msg)
            
              t1=float(rospy.Time.now().to_sec())
             
              current_distance= speed*(t1-t0)
          #After the loop, stops the robot
          #if (current_distance=distance):
                   # angle()
          vel_msg.linear.x = 0
          
                    
          #Force the robot to stop
          pub.publish(vel_msg)
          return angle()
          

movex()
movey()
movex2()
movey()
'''def end():
    if movex()==True:
         movey()


end()


   '''


          
         
      