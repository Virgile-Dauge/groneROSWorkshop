#! /usr/bin/env python
import rospy

import actionlib
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
import my_pkg.msg

class reach_positionAction(object):
    # create messages that are used to publish feedback/result
    _feedback = my_pkg.msg.reach_positionFeedback()
    _result = my_pkg.msg.reach_positionResult()

    def __init__(self, name):
        self._action_name = 'turtle_action'
        self._as = actionlib.SimpleActionServer(self._action_name, my_pkg.msg.reach_positionAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        max_speed = 5

        goal_pose = Pose()
        goal_pose.x = goal.x
        goal_pose.y = goal.y
        distance_tolerance = 0.5
        vel_msg = Twist()

        self._feedback.distance = 0

        # publish info to the console for the user
        rospy.loginfo("starting procedure to reach new goal")
        # start executing the action
        while self.get_distance(goal_pose.x,goal_pose.y) >= distance_tolerance:

            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break

            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * self.get_distance(goal_pose.x, goal_pose.y)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)

            self._feedback.distance = self.get_distance(goal_pose.x,goal_pose.y)
            # publish the feedback
            self._as.publish_feedback(self._feedback)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)

        if success:
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('turtle_action')
    server = reach_positionAction(rospy.get_name())
    rospy.loginfo("ready to receive goals")
    rospy.spin()
