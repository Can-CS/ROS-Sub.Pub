#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String


def callback(data):

	rospy.loginfo(data.data)

def subs():

	rospy.init_node('listener',anonymous=True)

	rospy.Subscriber('topic1',Int32, callback)

	rospy.spin()

if __name__ == '__main__':

	subs()
