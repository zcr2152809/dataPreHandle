import cv2
import numpy as np
import imutils
from skimage.metrics import structural_similarity as ssim

# Canny
def Canny(image):
    edges = cv2.Canny(image, 100, 200)
    edge_count = np.sum(edges > 0)
    return edge_count

def contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = np.std(gray)
    return contrast

def FFT(image):
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (h, w) = gray.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)
    fftShift[cY - 60:cY + 60, cX - 60:cX + 60] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)
    magnitude = 20 * np.log(np.abs(recon) + 1e-9)
    mean = np.mean(magnitude)
    return mean

def frequency(image):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1e-9)
    # 以高频成分的能量作为判断标准
    high_freq_energy = np.sum(magnitude_spectrum > 200)
    return high_freq_energy

def Laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    return fm

def SSIM(image):
    # 将图片转换为灰度图片
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 创建一个轻微模糊的版本作为比较对象
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # 获取图像的大小
    h, w = gray.shape
    # 根据图像大小动态调整win_size，确保它不大于图像的最小维度
    # 同时要求win_size为奇数
    win_size = min(11, h - 1 if h % 2 == 0 else h, w - 1 if w % 2 == 0 else w)
    # 计算SSIM，显式指定win_size
    score, _ = ssim(gray, blurred, win_size=win_size, full=True)
    return score