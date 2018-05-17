#! /usr/bin/env python
import rospy
from simple_pid import PID
import actionlib
from geometry_msgs.msg  import Twist
from nav_msgs.msg  import Odometry
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
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/pioneer_p3dx/odom', Odometry, self.callback)
        self.pose = Odometry().pose.pose
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data.pose.pose
        self.pose.position.x = round(self.pose.position.x, 4)
        self.pose.position.y = round(self.pose.position.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.position.x), 2) + pow((goal_y - self.pose.position.y), 2))
        return distance

    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        max_linear_speed = 1
        max_angular_speed = 0.1
        p = 1

        goal_pose = Pose()
        goal_pose.x = goal.x
        goal_pose.y = goal.y
        distance_tolerance = 1
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
            computed_linear_vel = p * self.get_distance(goal_pose.x, goal_pose.y)
            if computed_linear_vel > max_linear_speed :
                computed_linear_vel = max_linear_speed
            vel_msg.linear.x = computed_linear_vel
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            computed_angular_vel = 4 * (atan2(goal_pose.y - self.pose.position.y, goal_pose.x - self.pose.position.x) - self.pose.orientation.z)
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            if computed_angular_vel > max_angular_speed :
                computed_angular_vel = max_angular_speed
            vel_msg.angular.z = computed_angular_vel

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
