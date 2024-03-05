import cv2
from generate_pick_model import is_blurry_fuction

for i in range(1, 20):
    imgPath = '../images/clear/' + str(i) + '.jpg'
    image = cv2.imread(imgPath)
    print(is_blurry_fuction.FFT(image))

print('------------------------')

for i in range(1, 20):
    imgPath = '../images/ambiguous/' + str(i) + '.jpg'
    image = cv2.imread(imgPath)
    print(is_blurry_fuction.FFT(image))
