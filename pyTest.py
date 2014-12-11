#!/usr/bin/env python
from __future__ import division
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
from std_msgs.msg import ColorRGBA
file = open('test.txt', 'w')

def main():
	rospy.init_node('sub_pcl');

	processor = Processor()
	rospy.Subscriber('/camera/depth/points', PointCloud2, processor.callback, queue_size=1)
	rospy.spin()

class Processor(object):
	"""Computes and logs the time taken to process a point cloud."""
	def __init__(self):
		self.pub = rospy.Publisher('chatter_color', ColorRGBA)

	def callback(self, data):
		"""Computes the average point in a point cloud and saves timing info."""
		points = pc2.read_points(data, field_names=['x', 'y', 'z'],
								skip_nans=True)
		num_points = 0
		avg_x = 0
		avg_y = 0
		avg_z = 0

		for x, y, z in points:
			num_points += 1
			avg_x += x
			avg_y += y
			avg_z += z

	
		if num_points > 0:
			avg_x /= num_points
			avg_y /= num_points
			avg_z /= num_points

		self.pub.publish(avg_x,avg_y,avg_z,0)



	
class Mover():
	"""Moves based on published data"""
	def __init__(self):
		super(Mover, self).__init__()
		self.cmd = rospy.Publisher("/base_controller/command", Twist)
		self.motion = Twist()

	def callback(self, msg):
		#position = msg.pose.position
		self.motion.linear.x = vector[0]
		self.motion.linear.z = vector[2]

		print("here")
		self.cmd.publish(motion)	
if __name__ == '__main__':
	main()

'''
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist

cmd = rospy.Publisher("/atrv/motion", Twist)
motion = Twist()
def callback(msg):
    position = msg.pose.position
        if position.x < 1:
            motion.linear.x = +0.5
        if position.x > 2:
            motion.linear.x = -0.5
    cmd.publish(motion)

rospy.init_node("rostuto1")
rospy.Subscriber("/atrv/pose", PoseStamped, callback)
rospy.spin()

'''