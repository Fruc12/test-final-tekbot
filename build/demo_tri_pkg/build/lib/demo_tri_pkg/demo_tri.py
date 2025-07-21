import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class DemoTriNode(Node):
    def __init__(self):
        super().__init__('demo_tri_node')
        self.publisher_ = self.create_publisher(String, 'tri_topic', 10)
        self.get_logger().info('Node demo_tri lancé, publication en cours...')
        self.timer = self.create_timer(2.0, self.publish_data)

    def publish_data(self):
        colors = ['red', 'blue', 'green', 'yellow']
        color = random.choice(colors)
        battery = random.randint(20, 100)
        msg = String()
        msg.data = f"{color},{battery}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publié: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = DemoTriNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

