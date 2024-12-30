from dataprovider import CameraDataProvider

class ObjectDetectionTextRecognition:
    def __init__(self):
        self.camera = CameraDataProvider()

    def capture_image(self):
        return self.camera.get_image()

    def run(self):
        self.camera.display_image()