# CaptchaCV2
A simple proof of concept for beating outdated Captcha methods using only opencv and numpy

## Summery

Many outdated websites and mobile apps still use the following captcha method:

![image](https://github.com/jboirazian/CaptchaCV2/assets/21143405/e0f80433-8e73-4cb9-a5b3-6f65eb995c65)

While you might think that it can be solved with your favorite OCR framework , the reality is that it can be solved by using only [Template matching](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)


### Method

In order to perform to perform Template matching... we are gonna need templates. In the folder **/selected_patterns** you will find the 3 pairs 0 to 9 diggits.
These images were reconstructed from 1000 digits of the same number and position in order to obtain the real number without that sky blue jitter :

![image](https://github.com/jboirazian/CaptchaCV2/assets/21143405/75e70ec7-6f1a-4ce6-93b2-9ebf06ce5361) ![image](https://github.com/jboirazian/CaptchaCV2/assets/21143405/641b76f1-abc0-4802-b0ad-b7952faf7f60) ![image](https://github.com/jboirazian/CaptchaCV2/assets/21143405/47169727-ec31-4349-a487-bf2c0f9bc4b4)


## How to run it

+ Install numpy and cv2
+ git clone https://github.com/jboirazian/CaptchaCV2.git
+ python3 verify.py

### Example

```python3
import modules.digit_recogniton as dr
import cv2

if __name__ == "__main__":
    img=cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    print(dr.predict_number(image=img))
```

## Performance

Without the need of a GPU and with the provided image example , the prediction was achived in less than 5 ms on my PC.

I was also able to run in on an really old Android table using [Termux](https://termux.dev/en/) and got around 50 ms 





