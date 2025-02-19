import cv2
from PIL import Image
import numpy as np
import io

def preprocess_image_for_ocr(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to a fixed height while maintaining aspect ratio
    height = 800
    ratio = height / image.shape[0]
    width = int(image.shape[1] * ratio)
    resized_image = cv2.resize(image, (width, height))
    
    # Apply Gaussian blur to reduce noise and improve OCR accuracy
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)
    
    # Apply adaptive thresholding to get a binary image
    # binary_image = cv2.adaptiveThreshold(
    #     blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    # )
    binary_image = blurred_image
    cv2.imwrite('C:\\Users\\YQiao2\\Downloads\\B.jpg', binary_image)
    # Return the preprocessed image
    return binary_image
    

# Example usage
# binary_image =  preprocess_image_for_ocr('C:\\Users\\YQiao2\\Downloads\\A.jpg')
# cv2.imshow('Preprocessed Image', binary_image)
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()  # Close all OpenCV windows