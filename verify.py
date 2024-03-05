import modules.digit_recogniton as dr
import cv2


if __name__ == "__main__":
    img=cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    print(dr.predict_number(image=img))