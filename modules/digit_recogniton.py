import cv2
import numpy as np
import os


def predict_digit(digit: cv2.Mat, digit_pos: str):
    highiest_prediction_score = 0
    highiest_prediction_digit = -1
    directory = f'selected_patterns/{digit_pos}/'
    files = os.listdir(directory)
    image_files = [
        f"{directory}{file}" for file in files if file.endswith('.png')]
    cv2Images = [cv2.threshold(cv2.imread(image_file, cv2.IMREAD_GRAYSCALE),
                               128, 255, cv2.THRESH_BINARY)[1] for image_file in image_files]

    for index, cv2Image in enumerate(cv2Images):
        score = cv2.matchTemplate(digit, cv2Image, cv2.TM_CCOEFF_NORMED)[0][0]
        # print(f"Looks like {files[index]} by a score of {score}")
        if(score > highiest_prediction_score):
            highiest_prediction_score = score
            highiest_prediction_digit = files[index].replace(".png", "")

    return highiest_prediction_digit


def predict_number(image: cv2.Mat) -> str:
    # Split the image into three 30x50 images
    prediction = []
    folders = ("A", "B", "C")
    # Crop regions
    h, w = image.shape
    crop_regions = [
        (0, 0, int(w/3), h),
        (int(w/3), 0, int(w/3)*2, h),
        (int(w/3)*2, 0, int(w), h)
    ]

    # Initialize a list to store cropped images
    cropped_images = []

    # Iterate over crop regions and crop the image
    for region in crop_regions:
        x1, y1, x2, y2 = region
        cropped_image = image[y1:y2, x1:x2]  # Using array slicing to crop
        cropped_images.append(cropped_image)

    # Convert cropped_images list to tuple of numpy arrays
    digits = tuple(np.array(img) for img in cropped_images)
    for index, digit in enumerate(digits):
        prediction.append(predict_digit(digit=digit, digit_pos=folders[index]))
    return ''.join(prediction)
