import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color
import cv2

# 读取原始图像
image = io.imread('TW.jpg')

# 转换为灰度图像
grey_image = color.rgb2gray(image)

# 将灰度图像存储为使用cv2函数生成的灰度图像
# plt.imsave('grey_without_cv2.png', grey_image, cmap='gray')
image = cv2.imread("TW.jpg")    #先讀取圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #把image這個檔案從BGR轉成灰階，放到gray這個變數

# 二值化处理
threshold = 244  # 可根据需要调整阈值
binary_image = np.where(gray > threshold, 255, 0).astype(np.uint8)

# 显示四张图像：原始、使用函数的灰度、不使用函数的灰度、二值化

plt.imshow(image)
plt.title('Original Image')
plt.show()

plt.imshow(grey_image, cmap='gray')
plt.title('Grey Image without cv2')
plt.show()

cv2.imshow("gray", gray)
cv2.waitKey(0)             #等待 enter被按下
cv2.destroyAllWindows()    #關閉opencv開啟的視窗

plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.tight_layout()
plt.show()