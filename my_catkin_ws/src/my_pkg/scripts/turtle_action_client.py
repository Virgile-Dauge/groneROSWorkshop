#! /usr/bin/env python

from __future__ import print_function

import rospy
import sys
# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import my_pkg.msg
def feedback_callback(data):
    print(data)

def turtle_client(x,y):
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('turtle_action', my_pkg.msg.reach_positionAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = my_pkg.msg.reach_positionGoal(x,y)

    # Sends the goal to the action server.
    client.send_goal(goal,feedback_cb= feedback_callback)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('turtle_client_py')
        if len(sys.argv) == 3:
            input_x = int(sys.argv[1])
            input_y = int(sys.argv[2])
        else:
            sys.exit(1)
        result = turtle_client(input_x,input_y)

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
