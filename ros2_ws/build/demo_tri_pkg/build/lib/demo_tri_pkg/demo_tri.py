import rclpy
from rclpy.node import Node
import random
import requests  # pour envoyer les données à Flask

class DemoTriNode(Node):
    def __init__(self):
        super().__init__('demo_tri_node')
        self.timer = self.create_timer(2.0, self.publish_data)
        self.get_logger().info("Node demo_tri lancé, publication en cours...")

    def publish_data(self):
        color = random.choice(['red', 'green', 'blue', 'yellow'])
        battery = random.randint(0, 100)
        self.get_logger().info(f"Publié: {color},{battery}")

        # Envoi à l'API Flask
        try:
            response = requests.get(f"http://127.0.0.1:5000/api/set?color={color}&battery={battery}")
            if response.status_code != 200:
                self.get_logger().warn(f"Erreur API Flask: {response.status_code}")
        except Exception as e:
            self.get_logger().error(f"Impossible d'envoyer au Flask: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DemoTriNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

