import cv2
from ImageHandler import ImageHandler

if __name__ == "__main__":
    try:
        image = cv2.imread('images/panzoom executing.png', 1)
        handler = ImageHandler(img=image)
    except KeyboardInterrupt:
        print('KeyboardInterrupted')
    finally:
        print('bye')