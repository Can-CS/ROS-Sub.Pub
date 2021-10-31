#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def publisher():

	x = 0
	pub = rospy.Publisher('topic1',Int32,queue_size = 10)
	rospy.init_node('publisher_node',anonymous=False)
	rate = rospy.Rate(10) # 10 hz
	while not rospy.is_shutdown():
		if(x <=2022):
			msg = x
			x = x + 1
			rospy.loginfo(msg)
			pub.publish(msg)
			rate.sleep()
		
if __name__ == "__main__":
	publisher()
		
