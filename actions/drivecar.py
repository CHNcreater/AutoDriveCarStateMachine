import sys
sys.path.append("..")
from .objectdetectiontextrecognition import ObjectDetectionTextRecognition
from dataprovider.dp_camera import CameraDataProvider
from .linedetection import line_detection
from communication.mqtt_client import MqttClient

def navigate_on_autopilot(ip_addr):
    """navigate on autopilot
    """
    return False
    data_provider = CameraDataProvider(ip_addr=ip_addr)
    image = data_provider.get_image()
    steering_angle = line_detection(image)

    

def drive_car():
    """drive the car
    """
    # 1. auto drive the car to the bifurcation

    # 2. detect the target mark
    odt = ObjectDetectionTextRecognition()
    image = odt.camera.get_image()
    target = odt.main(image)