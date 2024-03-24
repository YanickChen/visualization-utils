"""
@Author: ChenYk
@Contact: Yinkang_chen@163.com
@File: hog_rgb.py
@Date: 2024/3/34 20:18
@Desc: 生成RGB值直方图
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 读取图像
image = cv2.imread('test.jpg')

# 将图像从BGR颜色空间转换为RGB颜色空间
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 计算RGB直方图
hist_r, bins_r = np.histogram(image_rgb[:,:,0].ravel(), bins=256, range=[0,256])
hist_g, bins_g = np.histogram(image_rgb[:,:,1].ravel(), bins=256, range=[0,256])
hist_b, bins_b = np.histogram(image_rgb[:,:,2].ravel(), bins=256, range=[0,256])

# 绘制RGB直方图
rcParams['font.family'] = 'SimHei'  # 中文支持
plt.figure()
plt.title('RGB直方图')
plt.xlabel('像素值')
plt.ylabel('像素频数')
# plt.title('RGB Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
plt.plot(hist_r, color='red', label='Red', alpha=0.7)
plt.plot(hist_g, color='green', label='Green', alpha=0.7)
plt.plot(hist_b, color='blue', label='Blue', alpha=0.7)
plt.legend()
plt.xlim([0, 256])
plt.savefig('./output/hog_rgb.jpg')
plt.show()

