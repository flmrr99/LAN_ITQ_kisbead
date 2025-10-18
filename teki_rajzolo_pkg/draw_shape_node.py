import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class DrawShapeNode(Node):
    def __init__(self):
        super().__init__('draw_shape')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Kérj be alakzatot
        self.shape_name = input("Válassz egy alakzatot (triangle/square/circle): ").strip().lower()

    def move_forward(self, distance, speed=1.0):
        vel_msg = Twist()
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0.0
        duration = distance / speed
        self._publish_for_duration(vel_msg, duration)

    def rotate(self, angle, angular_speed=math.pi/2):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = angular_speed if angle > 0 else -angular_speed
        duration = abs(angle) / angular_speed
        self._publish_for_duration(vel_msg, duration)

    def _publish_for_duration(self, vel_msg, duration):
        end_time = time.time() + duration
        rate = 20  # Hz
        while time.time() < end_time:
            self.publisher_.publish(vel_msg)
            time.sleep(1.0 / rate)

    def draw_shape(self):
        if self.shape_name == 'triangle':
            for _ in range(3):
                self.move_forward(2.0)
                self.rotate(2 * math.pi / 3)
        elif self.shape_name == 'square':
            for _ in range(4):
                self.move_forward(2.0)
                self.rotate(math.pi / 2)
        elif self.shape_name == 'circle':
            vel_msg = Twist()
            vel_msg.linear.x = 1.5
            vel_msg.angular.z = 1.5
            self._publish_for_duration(vel_msg, 6.28)
        else:
            self.get_logger().info("Érvénytelen alakzat, triangle lesz az alapértelmezett.")
            self.shape_name = 'triangle'
            for _ in range(3):
                self.move_forward(2.0)
                self.rotate(2 * math.pi / 3)

        # Megállítás a végén
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)
        self.get_logger().info(f"{self.shape_name} elkészült!")

def main(args=None):
    rclpy.init(args=args)
    node = DrawShapeNode()
    node.draw_shape()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
