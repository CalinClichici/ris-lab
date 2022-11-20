#!/usr/bin/env python3

# CLICHICI CALIN CONSTANTIN

from __future__ import print_function

import rospy

from geometry_msgs.msg import Wrench

def handle_force_torque_push(req):
    req.x

def force_torque_service():
    rospy.init_node('force_torque_service')
    s = rospy.Service('force_torque_push', Wrench, handle_force_torque_push)
    rospy.spin()