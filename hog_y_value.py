"""
@Author: ChenYk
@Contact: Yinkang_chen@163.com
@File: hog_y_value.py
@Date: 2024/3/34 20:18
@Desc: 生成Y值直方图
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 读取图像
image = cv2.imread('test.jpg')

# 将图像从BGR颜色空间转换为YUV颜色空间
image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# 提取亮度分量Y
y_channel = image_yuv[:,:,0]

# 计算Y值直方图
hist_y, bins_y = np.histogram(y_channel.ravel(), bins=256, range=[0,256])

# 绘制Y值直方图
rcParams['font.family'] = 'SimHei'  # 中文支持
plt.figure()
plt.title('Y直方图')
plt.xlabel('像素值')
plt.ylabel('像素频数')
# plt.title('Y Value Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
plt.plot(hist_y, color='gray', label='Y', alpha=0.7)
plt.legend()
plt.xlim([0, 256])
plt.show()
