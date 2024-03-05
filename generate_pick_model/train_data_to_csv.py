import cv2
import is_blurry_fuction
import pandas as pd

train_data = {
    'Canny': [],
    'contrast': [],
    'FFT': [],
    'frequency': [],
    'Laplacian': [],
    'SSIM': [],
    'is_blurry': []
}

for i in range(1, 201):
    clearImagePath = '../images/clear/' + str(i) + '.jpg'
    clearImage = cv2.imread(clearImagePath)
    train_data['Canny'].append(is_blurry_fuction.Canny(clearImage))
    train_data['contrast'].append(is_blurry_fuction.contrast(clearImage))
    train_data['FFT'].append(is_blurry_fuction.FFT(clearImage))
    train_data['frequency'].append(is_blurry_fuction.frequency(clearImage))
    train_data['Laplacian'].append(is_blurry_fuction.Laplacian(clearImage))
    train_data['SSIM'].append(is_blurry_fuction.SSIM(clearImage))
    train_data['is_blurry'].append(0)

    ambiguousImagePath = '../images/ambiguous/' + str(i) + '.jpg'
    ambiguousImage = cv2.imread(ambiguousImagePath)
    train_data['Canny'].append(is_blurry_fuction.Canny(ambiguousImage))
    train_data['contrast'].append(is_blurry_fuction.contrast(ambiguousImage))
    train_data['FFT'].append(is_blurry_fuction.FFT(ambiguousImage))
    train_data['frequency'].append(is_blurry_fuction.frequency(ambiguousImage))
    train_data['Laplacian'].append(is_blurry_fuction.Laplacian(ambiguousImage))
    train_data['SSIM'].append(is_blurry_fuction.SSIM(ambiguousImage))
    train_data['is_blurry'].append(1)

df = pd.DataFrame(train_data)

df.to_csv('../tools/train_data.csv', index=True)