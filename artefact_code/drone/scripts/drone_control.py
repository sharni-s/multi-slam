import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

def control_message(cmd_str):
    twist_msg = Twist()
    if cmd_str == 'move_forward':
        twist_msg.linear.z = 0.2
    elif cmd_str == 'move_backward':
        twist_msg.linear.z = -0.2
    elif cmd_str == 'move_left':
        twist_msg.linear.y = 0.2
    elif cmd_str == 'move_right':
        twist_msg.linear.y = -0.2
    elif cmd_str == 'go_up':
        twist_msg.linear.x = 0.2
    elif cmd_str == 'go_down':
        twist_msg.linear.x = -0.2
    elif cmd_str == 'turn_left':
        twist_msg.angular.z = 0.2
    elif cmd_str == 'turn_right':
        twist_msg.angular.z = -0.2
    return twist_msg


def autonomous_control():

    self.pub_takeoff = rospy.Publisher(
        'takeoff', Empty, queue_size=1, latch=False)
    self.pub_land = rospy.Publisher(
        'land', Empty, queue_size=1, latch=False)
    self.pub_emergency = rospy.Publisher(
        'emergency', Empty, queue_size=1, latch=False)
    self.pub_cmd_out = rospy.Publisher(
        'cmd_vel', Twist, queue_size=10, latch=False)

    rospy.init_node('drone_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Takeoff
        self.pub_takeoff.publish()
        time.sleep(2)

        # Start moving through the course
        self.pub_cmd_out.publish(control_message('go_up'))
        time.sleep(1)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(3)
        self.pub_cmd_out.publish(control_message('turn_left'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(2)
        self.pub_cmd_out.publish(control_message('turn_left'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('turn_right'))
        time.sleep(1)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(3)
        self.pub_cmd_out.publish(control_message('turn_right'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(3)
        self.pub_cmd_out.publish(control_message('turn_right'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(4.5)
        self.pub_cmd_out.publish(control_message('turn_right'))
        time.sleep(0.5)
        self.pub_cmd_out.publish(control_message('move_forward'))
        time.sleep(0.5)

        # End of course
        self.pub_land.publish()

if __name__ == '__main__':
    try:
        autonomous_control()
    except rospy.ROSInterruptException:
        pass
