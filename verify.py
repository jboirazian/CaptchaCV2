import modules.digit_recogniton as dr
import cv2
import time


if __name__ == "__main__":

    img=cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)

    start_time = time.time()
    print(dr.predict_number(image=img))
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Time taken:", elapsed_time, "seconds")