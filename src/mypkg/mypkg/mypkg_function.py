import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from rclpy.qos import qos_profile_sensor_data
import cv2
from cv_bridge import CvBridge, CvBridgeError

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
			Image,
			'/image_raw',
			self.listener_callback,
			qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning
        self.value = 0
        self.bridge = CvBridge()

    def listener_callback(self, image):
        print("In callback")
        cv_image = self.bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')
        cv2.imshow('mywindowze', cv_image)
        k = cv2.waitKey(30) & 0xff

        #Press 'c' to save frame
        if k == 99:
            filename = '/home/andrea/Desktop/Capture_'+str(self.value)+'.jpg'
            cv2.imwrite(filename, cv_image)
            self.value+=1

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    print("Hello!")
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()
    print("Goodbye!")

if __name__ == '__main__':
    main()
