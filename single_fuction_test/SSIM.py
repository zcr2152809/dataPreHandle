import cv2
from generate_pick_model import is_blurry_fuction

for i in range(1, 20):
    # 读取图片
    imagePath = '../images/clear/' + str(i) + '.jpg'
    image = cv2.imread(imagePath)
    print(is_blurry_fuction.SSIM(image))

print('--------------------')

for i in range(1, 20):
    # 读取图片
    imagePath = '../images/ambiguous/' + str(i) + '.jpg'
    image = cv2.imread(imagePath)
    print(is_blurry_fuction.SSIM(image))