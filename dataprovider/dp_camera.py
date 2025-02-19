import requests
from PIL import Image
from io import BytesIO
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from configuration import Configuration

class CameraDataProvider:
    def __init__(self, ip_addr):
        self.configuration = Configuration()
        self.server_url = "http://" + ip_addr + self.configuration.get("camera", "server_url")

    def get_image(self):
        try:
            response = requests.get(self.server_url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")
            return None

    def display_image(self):
        image_data = self.get_image()
        if image_data:
            import matplotlib.pyplot as plt

            image = Image.open(BytesIO(image_data))
            plt.imshow(image)
            plt.axis('off')  # Hide axes
            plt.show()
        else:
            print("No image data to display.")


# Example usage:
if __name__ == '__main__':
    camera = CameraDataProvider()
    camera.display_image()