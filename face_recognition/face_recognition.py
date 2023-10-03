

import cv2
import numpy as np


def _preprocess_image(image):
    resized_image = cv2.resize(image, (64, 64))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = gray_image / 255.0
    return normalized_image




if __name__ == '__main__':
    # You can add a test case or example usage of the FaceRecognition class here
    pass
