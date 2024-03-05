import cv2
from generate_pick_model import is_blurry_fuction

# 加载图像
for i in range(1, 20):
    # 读取图片
    imagePath = '../images/clear/' + str(i) + '.jpg'
    image = cv2.imread(imagePath)
    # 应用Canny边缘检测
    print(is_blurry_fuction.Canny(image))

print('----------------------')

for i in range(1, 20):
    # 读取图片
    imagePath = '../images/ambiguous/' + str(i) + '.jpg'
    image = cv2.imread(imagePath)
    # 应用Canny边缘检测
    print(is_blurry_fuction.Canny(image))
