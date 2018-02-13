#!/usr/bin/env python

## Pilote pionneer 

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

pubG = rospy.Publisher('/pioneer_p3dx/leftWheelCommand', Float64, queue_size=10)
pubD = rospy.Publisher('/pioneer_p3dx/rightWheelCommand', Float64, queue_size=10)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    lin = data.linear
    ang = data.angular
    print("lin = %f %f %f" % (lin.x, lin.y, lin.z))
    print("ang = %f %f %f" % (ang.x, ang.y, ang.z))
    wl = (lin.x - ang.z * 0.33 / 2.0) / 0.1
    wr = (lin.x + ang.z * 0.33 / 2.0) / 0.1
    print("wl = %f wr = %f" % (wl, wr))
    pubG.publish(Float64(wl))
    pubD.publish(Float64(wr))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pioneer_driver', anonymous=True)

    rospy.Subscriber('cmd_vel', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
