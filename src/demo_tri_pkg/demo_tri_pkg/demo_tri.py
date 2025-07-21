import rclpy
from rclpy.node import Node
import random
import requests  # pour envoyer les données à Flask

class DemoTriNode(Node):
    def __init__(self):
        super().__init__('demo_tri_node')
        self.timer = self.create_timer(8.0, self.publish_data)
        self.get_logger().info("Node demo_tri lancé, publication en cours...")

    def publish_data(self):
        color = random.choice(['red', 'green', 'blue', 'yellow'])
        battery = random.randint(0, 100)
        self.get_logger().info(f"Publié: {color},{battery}")

        # Envoi à l'API Flask
        try:
            url = f"http://127.0.0.1:5000/api/set?color={color}&battery={battery}"
            response = requests.get(url)
            if response.status_code == 200:
                self.get_logger().info("[demo_tri_node] Flask API updated successfully")
            else:
                self.get_logger().warn(f"[demo_tri_node] Flask API update failed: {response.status_code}")
        except Exception as e:
            self.get_logger().error(f"[demo_tri_node] Exception calling Flask API: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DemoTriNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

